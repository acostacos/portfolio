from django.views.generic import ListView

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    context_object_name = 'projects'
    # paginate_by = 6
    # ordering = ['-created_at']
