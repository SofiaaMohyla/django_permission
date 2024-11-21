from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import Project


class ProjectListView(PermissionRequiredMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'
    permission_required = 'some_app.view_project'


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_edit.html'
    permission_required = 'some_app.edit_project'

    def get_success_url(self):
        return reverse_lazy('project_list')
