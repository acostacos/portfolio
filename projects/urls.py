from django.urls import path
from projects.views.project_list_view import ListView
from projects.views.project_detail_view import DetailView

app_name = 'projects'
urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]
