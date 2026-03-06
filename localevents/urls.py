from django.urls import path

from .views import *

urlpatterns = [
    path('localevents/events', EventListView.as_view(), name='event_list'),
    path('localevents/event/<int:pk>', EventDetailView.as_view(),
         name='event_detail'),
]

app_name = 'localevents'
