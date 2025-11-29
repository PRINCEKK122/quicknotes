from django.contrib import admin

from .models import Collection, Note

admin.site.register(Note)
admin.site.register(Collection)
