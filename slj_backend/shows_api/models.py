from django.db import models

# Create your models here.

class Show(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    videofile = models.FileField(upload_to='shows/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)