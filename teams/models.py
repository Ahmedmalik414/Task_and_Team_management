from django.db import models
from accounts import models as accounts


class Team(models.Model):
    team_name= models.CharField(max_length=30)
    
    def __str__(self):
        return self.team_name
    
    
    
class Team_member(models.Model) :
    team = models.ForeignKey(Team, on_delete=models.CASCADE) 
    user = models.ForeignKey(accounts.CustomUser, on_delete=models.CASCADE)
    role= models.CharField(max_length=30)
    
    
    def __str__(self):
       return f"{self.user.username} - {self.team.team_name}"
     
    
