from django.db import models



# Create your models here.


class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    locattion=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Employes(models.Model):
    Name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    phone_number=models.IntegerField()
    date_of_birth=models.DateField()
    Post=models.CharField(max_length=20)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.Name,self.last_name,self.age)