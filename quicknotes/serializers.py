from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quicknotes.models import Collection, Note


class CollectionSerializer(ModelSerializer):
    # notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = "__all__"


class NoteSerializer(ModelSerializer):
    # collection = CollectionSerializer(many=False, read_only=True)
    collection_name = serializers.CharField(source="collection.name", read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
