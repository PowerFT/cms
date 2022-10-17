from django.db import models

# Create your models here.
class Client(models.Model):
    mainid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=30)
    contactperson = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    countryname = models.CharField(max_length=20)
    cityname = models.CharField(max_length=25)
    address = models.TextField()
    dateandtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.companyname} {self.contactperson}"

class Project(models.Model):
    mainid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    amount = models.FloatField()
    clientname = models.ForeignKey(Client, on_delete=models.CASCADE)
    startdate = models.DateField()
    duedate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.clientname.companyname}"







