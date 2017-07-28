from django.shortcuts import render
from django.views.generic.base import TemplateView
from organizations.models import Organization


# Create your views here.
class Organizations(TemplateView):
    template_name = "organizations/master_list.html"
    
    def get(self, request):
        context = {}
        context['organizations'] = Organization.objects.order_by('orgName')
        return render(request, self.template_name, context)
    