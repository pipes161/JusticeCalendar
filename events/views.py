import datetime

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView

from events.models import Event


class Updates(TemplateView):
    template_name = "events/updates.html"
    
    def get(self, request):        
        ignore_before = datetime.datetime(2017, 1, 28, 0, 30, 0, 0, timezone.pytz.timezone("US/Eastern"))
        
        context = {}
        # the number 3 for action_flag signifies a deletion
        context['log_entries'] = LogEntry.objects.filter(action_time__gte = ignore_before,
                                                         content_type=ContentType.objects.get(model="event")).exclude(action_flag=3)
        return render(request, self.template_name, context)

# Create your views here.
class OneWeek(TemplateView):
    template_name = "events/index.html"
    
    def get(self, request, firstDay=None, *args, **kwargs):
        start_date = timezone.localtime(
                                      timezone.now(),
                                      timezone=timezone.pytz.timezone("US/Eastern")).date()
        if firstDay is not None:
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
