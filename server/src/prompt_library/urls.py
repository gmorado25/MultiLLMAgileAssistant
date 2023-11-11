from django.urls import path
from prompt_library.views.function_based_views import prompt_detail, prompt_list, format_list
from prompt_library.views.prompt_search import PromptSearch

urlpatterns = [
    path('prompts/', prompt_list, name='prompts'),
    path('prompts/<int:id>/', prompt_detail, name='prompt_id'),
    path('prompts/search/', PromptSearch.as_view(), name='prompt_search'),
    path('formats/', format_list, name='formats')
]