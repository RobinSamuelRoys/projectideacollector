from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Project_list=(
    (0,'Mini project'),
    (1,'Main Project'),
    (2,'Live Project')
)

class Master(models.Model):
    created_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    class Meta:
        abstract=True



class Course(Master):
    course=models.CharField(max_length=50)

    def __str__(self):
        return self.course
    
class Technology(Master):
    Technology=models.CharField(max_length=100)

    def __str__(self):
        return self.Technology
    
class Project_ideas(Master):
    course=models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE)
    Project_type=models.IntegerField(choices=Project_list,null=False,blank=False)
    Discription=models.TextField()
    Technology=models.ManyToManyField(Technology,null=True,blank=True)
    Project_Title=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.Project_Title
    



    

