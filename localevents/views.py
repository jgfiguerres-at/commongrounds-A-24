from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = 'localevents/event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'localevents/event_detail.html'
    context_object_name = 'event'
