"""repository URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from papers import views as papers_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', papers_views.PapersList.as_view(), name='list'),
    re_path('results/$', papers_views.Results.as_view(), {'category': None}, name='results'),
    re_path('results/(?P<category>\w{0,50})/$', papers_views.Results.as_view(), name='results'),
    path('keywords/', papers_views.keywords, name='keywords'),
    path('bibliography/', papers_views.bibliography, name='bibliography'),
    path('', papers_views.Home.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
