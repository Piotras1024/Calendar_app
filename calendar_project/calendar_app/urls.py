from django.urls import path
from . import views

urlpatterns = [
    # main page
    path('', views.calendar_view, name='calendar_view'),
    path('calendar/events-json/', views.events_json, name='events_json'),  # Ścieżka do JSON z wydarzeniami
]