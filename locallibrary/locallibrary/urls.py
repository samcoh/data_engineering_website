"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls import url

from django.contrib.auth import views as auth_views

from django.views.generic import RedirectView

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.admin_approval.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('catalog/', include('catalog.urls')),
    #path('', RedirectView.as_view(url='/catalog/', permanent=True)),

]

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Keep everything below this line

if 'crispy_forms' in settings.INSTALLED_APPS :
    urlpatterns += [
        path('', include('catalog.urls')),
    ]

# if 'rest_framework' in settings.INSTALLED_APPS :
#     urlpatterns += [
#         path('rest/', include('rest.urls')),
#     ]

if 'social_django' in settings.INSTALLED_APPS :
    urlpatterns += [
        url(r'^oauth/', include('social_django.urls', namespace='social')),
    ]

# Serve the favicon
import os
from django.views.static import serve
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]
