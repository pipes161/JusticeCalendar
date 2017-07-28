from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$', message="Phone number must be entered in the format: '999-999-9999'. Up to 15 digits allowed.")

# Create your models here.
class Organization(models.Model):
    addedAt = models.DateTimeField(auto_now_add=True, verbose_name="Added on")
    lastEditedAt = models.DateTimeField(auto_now=True, verbose_name="Last Edit on")
    currentlyActive = models.BooleanField(default=True, verbose_name="This organization is currently operating")
    
    orgName = models.CharField(max_length=200, verbose_name="Organization Name")
    description = models.TextField(blank=True, verbose_name="Organization Description")
    descriptionApproved = models.BooleanField(default=False, verbose_name="Description has been approved by the organization")
    affilatedVT = models.BooleanField(default=False, verbose_name="This organization has a formal affiliation with Virginia Tech")
    
    contactEmail = models.CharField(max_length=200, blank=True, verbose_name="Contact Email")
    contactPhone = models.CharField(max_length=200, blank=True, verbose_name="Contact Phone Numbers", validators=[phone_regex])
    
    facebookPage = models.URLField(blank=True, verbose_name="Organization Facebook page")
    twitter = models.URLField(blank=True, verbose_name="Organization Twitter")
    youtube = models.URLField(blank=True, verbose_name="Organization YouTube")
    website = models.URLField(blank=True, verbose_name="Organization Website")
    
    def __str__(self):
        return self.orgName