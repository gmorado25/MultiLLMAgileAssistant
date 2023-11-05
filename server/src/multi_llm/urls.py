from django.urls import path
from multi_llm.views.llm_query import LLMQuery
from multi_llm.views.function_based_views import llm_list

urlpatterns = [
    path('models/', llm_list, name='models'),
    path('generate/', LLMQuery.as_view(), name='generate'),
]