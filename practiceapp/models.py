from django.db import models
class Job(models.Model):

    jobtitle = models.CharField(max_length=100)

    jobdescription = models.CharField(max_length=500)


