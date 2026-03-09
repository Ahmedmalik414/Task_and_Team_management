from django.db import models
from accounts import models as accounts
from teams import Team
STATUS_CHOICES = [
    ("pending","Pending"),
    ("in_progress","In Progress"),
    ("completed","Completed"),
    ("blocked","Blocked")
]
class Project(models.Model):
    name = models.CharField(max_length=30)
    deadline= models.DateTimeField()
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    started = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=12,choices=STATUS_CHOICES)
    
    
    def __str__(self):
        return self.name
   





class Task(models.Model):
    task_title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    details = models.CharField(max_length=1500, blank=True, null=True)  
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(accounts.CustomUser, on_delete=models.CASCADE)
    started_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()  
    status= models.CharField(max_length=12,choices=STATUS_CHOICES)
    
    
    
    def __str__(self):
        return self.task_title