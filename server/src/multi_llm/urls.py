from django.urls import path
from multi_llm.views.llm_query import LLMQuery
from multi_llm.views.function_based_views import models

urlpatterns = [
    path('models/', models, name='models'),
    path('generate/', LLMQuery.as_view(), name='generate'),
]