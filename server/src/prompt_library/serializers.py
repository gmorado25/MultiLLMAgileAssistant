from rest_framework import serializers
from prompt_library.models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['title', 'description', 'sdlc_phase', 'role']

