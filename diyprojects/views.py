from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import ProjectCategory, Project


class ProjectListView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'diyprojects/project_list.html' # default value


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'diyprojects/project_detail.html' # default value