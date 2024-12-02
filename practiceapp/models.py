from django.db import models
class Job(models.Model):

    jobtitle = models.CharField(max_length=100)

    jobdescription = models.CharField(max_length=500)

class Country(models.Model):
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
class City(models.Model):
    city = models.ForeignKey(State, on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname


