from django.urls import path
from info.views.index_view import IndexView
from info.views.about_view import AboutView

app_name = 'info'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]
