from django.urls import path
from .views import ProjectListView, ProjectUpdateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('projects/edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_edit'),
]