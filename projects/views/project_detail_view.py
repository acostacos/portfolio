from django.views.generic import DetailView

class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    context_object_name = 'projects'
    # model = Project
