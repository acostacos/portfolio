from django.shortcuts import render

from django.views import View

class IndexView(View):
    template_name = 'info/index.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
