from django.db import models

class Events(models.Model):
    EVENTS_STATUS = (
         ('UPCOMING','upcoming'),
         ('DONE','done')
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='events/img')
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(choices=EVENTS_STATUS,default='UPCOMING',max_length=50)
    location = models.CharField(max_length=200)
    time = models.TimeField()
    
    def __str__(self):
        return self.events.title

