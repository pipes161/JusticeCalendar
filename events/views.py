import datetime

from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView

from events.models import Event


# Create your views here.
class OneWeek(TemplateView):
    template_name = "events/index.html"
    
    def get(self, request, firstDay=str(timezone.now().date()), *args, **kwargs):
        start_date = datetime.datetime.strptime(firstDay, "%Y-%m-%d").date()
        end_date = start_date + datetime.timedelta(days=6)
        
        context = {}
        
        context['events'] = Event.objects.filter(startDay__range=[start_date, end_date]).order_by('startDay', 'startTime')
        
        context['start_date'] = start_date
        context['end_date'] = end_date
        
        if start_date > timezone.now().date():
            context['previous_week'] = start_date - datetime.timedelta(days=7)
        
        if Event.objects.latest('startDay').startDay >= end_date + datetime.timedelta(days=1):
            context['next_week'] = end_date + datetime.timedelta(days=1)
        
        return render(request, self.template_name, context)