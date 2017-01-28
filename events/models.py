import datetime

from django.db import models


# Create your models here.
class Event(models.Model):
    # MANDATORY FIELDS
    title = models.CharField(max_length=200)
    startDay = models.DateField(db_index=True)
    startTime = models.TimeField(db_index=True)
    addedAt = models.DateTimeField(auto_now_add=True)
    lastEditedAt = models.DateTimeField(auto_now=True)
    
    # OPTIONAL FIELDS
    # Ending Time
    endDay = models.DateField(null=True, blank=True, db_index=True)
    endTime = models.TimeField(null=True, blank=True, db_index=True)
    
    # Description and Categorization
    description = models.TextField(blank=True)
    sponsors=models.TextField(blank=True)
    
    # Location Information
    address = models.CharField(max_length=200, blank=True)
    buildingRoom = models.CharField(max_length=200, blank=True)
    
    # Contact Information
    primaryContactName = models.CharField(max_length=200, blank=True)
    primaryContactEmail = models.CharField(max_length=200, blank=True)
    
    # External Links
    fbEventLink = models.URLField(blank=True)
    gobblerConnectLink = models.URLField(blank=True)
    announcementWebsite = models.URLField(blank=True)
    
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
