from django.urls import path

from .views import home_page, aboutus, blog, events, organizacion

app_name = 'home'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about', aboutus, name='about'),
    path('blog', blog, name='blog'),
    path('events', blog, name='events'),
    path('organization', organizacion, name='organization'),
]
