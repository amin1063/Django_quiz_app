from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,primary_key="true")
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
from django.db import models


class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)


class Person(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.CharField(max_length=10)
   eye_color = models.CharField(max_length=10)
   species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)    
        
    