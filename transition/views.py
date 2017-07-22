import datetime

from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView
from transition.models import Entry


# Create your views here.
class Timeline(TemplateView):
    template_name = "transition/timeline.html"
    
    def get(self, request):
        context = {}
        context['entries'] = Entry.objects.order_by('eventDay','sameDayOrder')
        return render(request, self.template_name, context)
    