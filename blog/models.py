from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(blank=False,null=False,max_length=20)
    birthday = models.DateTimeField(blank=False,null=False)
    gender = models.CharField(blank=False,null=False,max_length=1)
    bloodtype = models.CharField(blank=False,null=False,max_length=2)
    profile = models.CharField(blank=False,null=False,max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name