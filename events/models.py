import datetime

from django.db import models


# Create your models here.
class Event(models.Model):
    # MANDATORY FIELDS
    title = models.CharField(max_length=200, verbose_name="Title")
    startDay = models.DateField(db_index=True, verbose_name="Start Date")
    startTime = models.TimeField(db_index=True, verbose_name="Start Time")
    addedAt = models.DateTimeField(auto_now_add=True, verbose_name="Added on")
    lastEditedAt = models.DateTimeField(auto_now=True, verbose_name="Last Edit at")
    
    # OPTIONAL FIELDS
    # Ending Time
    endDay = models.DateField(null=True, blank=True, db_index=True, verbose_name="End Day")
    endTime = models.TimeField(null=True, blank=True, db_index=True, verbose_name="End Time")
    
    # Description and Categorization
    description = models.TextField(blank=True, verbose_name="Description")
    sponsors=models.TextField(blank=True, verbose_name="Sponsors")
    
    # Location Information
    address = models.CharField(max_length=200, blank=True, verbose_name="Street Address")
    buildingRoom = models.CharField(max_length=200, blank=True, verbose_name="Building Name and Room Number")
    
    # Contact Information
    primaryContactName = models.CharField(max_length=200, blank=True, verbose_name="Primary Contact Name")
    primaryContactEmail = models.CharField(max_length=200, blank=True, verbose_name="Primary Contact Email")
    
    # External Links
    fbEventLink = models.URLField(blank=True, verbose_name="Facebook Event Link")
    gobblerConnectLink = models.URLField(blank=True, verbose_name="GobblerConnect Event Link")
    announcementWebsite = models.URLField(blank=True, verbose_name="Event Website")
    
    def __str__(self):
        return self.title

    def googleCalendarLink(self):
        link = ("https://www.google.com/calendar/render?action=TEMPLATE"
              "&text={}"
              "&dates={}/{}"
              "&details={}{}"
              "&location={}"
              "&sf=true&output=xml")
        return link.format(self.title,
                        self._googleCalendarStartDay(),
                        self._googleCalendarEndDay(),
                        self.buildingRoom + ' : ' if self.buildingRoom else '',
                        self.description,
                        self.address)

    def _googleCalendarStartDay(self):
        return datetime.datetime.combine(self.startDay, self.startTime).strftime("%Y%m%dT%H%M%S")
    
    def _googleCalendarEndDay(self):
        endDay = self.endDay if self.endDay else self.startDay
        end = datetime.datetime.combine(endDay, self.endTime) if self.endTime else datetime.datetime.combine(endDay, self.startTime) + datetime.timedelta(hours=1)
#         print(end)
        return end.strftime("%Y%m%dT%H%M%S")
    
    def save(self, *args, **kwargs):
        if not self.endDay:
            self.endDay = self.startDay
        if not self.endTime:
            endDateTime = datetime.datetime.combine(self.endDay, self.startTime) + datetime.timedelta(hours=1)
            self.endTime = endDateTime.time()
            self.endDay = endDateTime.date()
        super(Event, self).save(*args, **kwargs)
