from django.db import models
from accounts import models as accounts
STATUS_CHOICES = [
    ("pending","Pending"),
    ("in_progress","In Progress"),
    ("completed","Completed"),
    ("blocked","Blocked")
]
class Projects(models.Model):
    name = models.CharField(max_length=30)
    deadline= models.DateTimeField(auto_now=True)
    started = models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=12,choices=STATUS_CHOICES)





class tasks(models.Model):
    task_title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    details = models.CharField(max_length=1500, blank=True, null=True)  
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(accounts.Users, on_delete=models.CASCADE)
    started_on= models.DateTimeField(auto_now=True)
    due = models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=12,choices=STATUS_CHOICES)