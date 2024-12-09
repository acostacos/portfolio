from django.shortcuts import render

from django.views import View

class IndexView(View):
    template_name = 'info/index.html'

    def get(self, request):
        header = 'Learn with Tacos'
        subheader = 'Machine Learning | Software Engineering'
        image_url = 'images/brain.png'
        context = {'header': header, 'subheader': subheader, 'image_url': image_url}
        return render(request, self.template_name, context)
