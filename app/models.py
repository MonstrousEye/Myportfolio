from django.db import models



# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default="")
    subject=models.CharField(max_length=50,default="")
    
    desc=models.CharField(max_length=500,default="")
    
    
    def __str__(self):
        return str(self.sno)+ " " + self.name + " " + self.email