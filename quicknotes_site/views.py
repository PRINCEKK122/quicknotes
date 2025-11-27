from django.shortcuts import render, get_object_or_404, redirect
from quicknotes.models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST


# data = [
#     {"name": "note1", "content": "This is my first note"},
#     {"name": "note2", "content": "This is my second note"},
#     {"name": "note3", "content": "This is my third note"},
# ]


def notes(request):
    data = Note.objects.all()
    return render(request, "quicknotes_site/index.html", {"notes": data, "form": NoteForm})

def note(request, note_id):
    # data = Note.objects.get(pk=note_id)
    data = get_object_or_404(Note, pk=note_id)
    note_form = NoteForm(instance=data)
    return render(request, "quicknotes_site/note.html", {"note": data, "form": note_form})

@require_POST
def add(request):
    # if request.method == "POST":
    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('notes')
    # return HttpResponse(status=405)

@require_POST
def edit(request, note_id):
    # if request.method == "POST":
    note = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
    return redirect('note', note_id=note.id)
    # return HttpResponse(status=405)

@require_POST
def delete(request, note_id):
    # if request.method == "POST":
    note = get_object_or_404(Note, pk=note_id)
    print(">>>>>>>>>>>>>", note)
    note.delete()
    return redirect("notes")
    # return HttpResponse(status=405)
