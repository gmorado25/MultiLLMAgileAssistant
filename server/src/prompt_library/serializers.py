from rest_framework import serializers
from prompt_library.models import Format, Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['title', 'description', 'sdlc_phase', 'role']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['title', 'description', 'sdlc_phase', 'role']


