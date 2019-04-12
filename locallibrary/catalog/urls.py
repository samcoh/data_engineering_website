from django.urls import path
from . import views
from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='catalog'),
    path('people/', views.PeopleListView.as_view(), name = 'people'),
    path('people/<int:pk>', views.PeopleDetailView.as_view(), name='people-detail'),
    path('project/', views.ProjectListView.as_view(), name = 'project'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/create',
        views.ProjectCreateView.as_view(success_url=reverse_lazy('catalog')), name='project_create'),
    path('project/<int:pk>/update',
        views.ProjectUpdateView.as_view(success_url=reverse_lazy('catalog')), name='project_update'),
    path('project/<int:pk>/delete',
        views.ProjectDeleteView.as_view(success_url=reverse_lazy('catalog')), name='project_delete'),

    path('people/create',
        views.PeopleCreateView.as_view(success_url=reverse_lazy('catalog')), name='people_create'),
    path('people/<int:pk>/update',
        views.PeopleUpdateView.as_view(success_url=reverse_lazy('catalog')), name='people_update'),
    path('people/<int:pk>/delete',
        views.PeopleDeleteView.as_view(success_url=reverse_lazy('catalog')), name='people_delete'),
]
# New lines below to serve static files in debug mode
import os
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'catalog/static'),
    }),
]
