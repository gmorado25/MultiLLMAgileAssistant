from django.http import HttpRequest
from rest_framework.response import Response
from django_nextjs.render import render_nextjs_page_sync

"""
URL configuration for the multillm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


def syncNextJS(request: HttpRequest) -> Response:
    return render_nextjs_page_sync(request)\
    
urlpatterns = [
    path('', include('django_nextjs.urls')),
    path('', syncNextJS, name='homepage'),
    path('dashboard/', syncNextJS, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', include('prompt_library.urls')),
    path('', include('multi_llm.urls')),
    path('', include('jira.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)