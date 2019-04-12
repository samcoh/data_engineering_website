from django.shortcuts import render

# Create your views here.
from catalog.models import People, Project
from django.views import View
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

#from catalog.util import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
def index(request):
    '''View Function for home page site'''
    list_people = People.objects.all()
    num_people = People.objects.all().count()
    context = {
        'num_people': num_people,
        'list_people': list_people,
    }
    return render(request, 'index.html', context = context)
from django.views import generic

class PeopleListView(generic.ListView):
    model = People
    # paginate_by = 100
    template_name = "catalog/people_list.html"

class PeopleDetailView(generic.DetailView):
    model = People
    # paginate_by = 100
    template_name = "catalog/people_detail.html"
class ProjectListView(generic.ListView):
    model = Project
    paginate_by =  100
    template_name = "catalog/project_list.html"
class ProjectDetailView(generic.DetailView):
    model = Project
    # paginate_by = 100
    template_name = "catalog/project_detail.html"

class ProjectCreateView(LoginRequiredMixin,generic.CreateView):
    model = Project
    fields = ['name','start_date', 'end_date', 'backend_progress', 'published', 'section', 'description', 'peoples']
    template_name = "catalog/project_form.html"

class ProjectUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Project
    fields = ['name','start_date', 'end_date', 'backend_progress', 'published', 'section', 'description','peoples']
    template_name = "catalog/project_form.html"

class ProjectDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Project
    #success_url = reverse_lazy('project')
    template_name = "catalog/project_confirm_delete.html"

class PeopleCreateView(LoginRequiredMixin,generic.CreateView):
    model = People
    fields = ['first_name','last_name', 'role','start_date','end_date', 'year_in_school', 'email',  "umich_id","phone_number", "projects", "majors", "minors", "picture" ]
    template_name = "catalog/people_form.html"

class PeopleUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = People
    fields = ['first_name','last_name', 'role', 'start_date','end_date','year_in_school', 'email',"umich_id", "phone_number", "projects", "majors", "minors"]
    #fields = ['name','start_date', 'end_date', 'published', 'section_id', 'description']
    template_name = "catalog/people_form.html"

class PeopleDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = People
    #success_url = reverse_lazy('project')
    template_name = "catalog/people_confirm_delete.html"

# class People_Projects_Many(TemplateView):
#     template_name = 'catalog/people_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['people_id'] = person_id.objects.all()
#         context['project_id'] = project_id.objects.all()
#         context['people_projects'] = People_Projects.objects.all()
#
#         return context
