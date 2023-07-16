from django.db import models

# Create your models here.
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    # gender = models.CharField(max_length=20)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id} / {self.name} / {self.email} / {self.mobile}"