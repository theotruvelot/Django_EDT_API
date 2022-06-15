from django.urls import path
from .views import loadWeek, load, index

urlpatterns = [
    path('reload', load, name='edt-reload'),
    # loadweek with week number in url
    path('', index, name='edt-loadweek'),
    path('<int:week>', loadWeek, name='edt-index'),
]