from django.urls import path
from jira.views.function_based_views import getResource

urlpatterns = [
    path('jira/', getResource, name='jira'),
]