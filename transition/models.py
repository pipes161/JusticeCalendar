from django.db import models

# Create your models here.
class Entry(models.Model):
    addedAt = models.DateTimeField(auto_now_add=True, verbose_name="Added on")
    lastEditedAt = models.DateTimeField(auto_now=True, verbose_name="Last Edit on")
    eventDay = models.DateField(db_index=True, verbose_name="Event Day")
    
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    
    sameDayOrder = models.IntegerField(blank=True, null=True, verbose_name="Order for same day events")
    
    def __str__(self):
        return self.title