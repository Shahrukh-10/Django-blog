from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=13)
    Issue = models.TextField()
    ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
