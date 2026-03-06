from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import ProjectCategory, Project


class ProjectListView(ListView):
    model = Project
    template_name = 'diyprojects/project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'diyprojects/project_detail.html'
    context_object_name = 'project'
