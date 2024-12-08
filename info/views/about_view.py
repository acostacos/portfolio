from django.shortcuts import render

from django.views import View

class AboutView(View):
    template_name = 'info/about.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
