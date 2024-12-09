from django.shortcuts import render

from django.views import View

class AboutView(View):
    template_name = 'info/about.html'

    def get(self, request):
        header = 'Hi, I\'m Tacos!'
        content = '''
        I am a software engineer by trade, but I prefer to introduce myself as a scientist. Driven by curiosity, I love tinkering with different technologies and finding applications of it no one has considered before. After discovering the capabilities of artificial intelligence, I decided to dedicate myself to learning everything I can about this field. I believe there are still so many use cases of AI that we yet to uncover. This website is my way of documenting my learning journey and sharing this to whoever finds it. Join me in my journey and let's learn together!
        '''
        context = {"header": header, "content": content}
        return render(request, self.template_name, context)
