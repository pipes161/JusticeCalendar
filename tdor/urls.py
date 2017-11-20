from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^2017/', TemplateView.as_view(template_name='tdor/2017.html'), name="tdor_2017"),
]
