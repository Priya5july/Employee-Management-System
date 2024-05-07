from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employes.objects.all()
    context={
        'emps':emps

    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method=='POST':
        print("post")
        Name=request.POST['Name']
        last_name=request.POST['last_name']
        age=(request.POST['age'])
        phone_number=(request.POST['phone_number'])
        date_of_birth=request.POST['date_of_birth']
        Post=request.POST['Post']
        role=request.POST['role']
        department=request.POST['department']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        hire_date=request.POST['hire_date']

        emps=Employes(Name=Name,last_name=last_name,age=age,phone_number=phone_number,date_of_birth=date_of_birth,Post=Post,role_id=role,department_id=department,salary=salary,bonus=bonus,hire_date=hire_date)
        emps.save()

        return render(request, 'add_emp.html', {'success_message': 'Employee Add Successfully'})

    elif request.method =='GET':
        print("get")
        return render(request,'add_emp.html')
          
    else :

        return render(request,'add_emp.html')



def remove_emp(request,emp_id=0):
    
    try:
        if emp_id:
            emps=Employes.objects.get(id=emp_id)
            emps.delete()
            return render(request, 'remove_emp.html', {'success_message': 'Employee Removed Successfully'})
    except:
        return HttpResponse("Enter valid Employee")
    emps=Employes.objects.all()
    context={
        'emps':emps

    }
    
    
    return render(request,'remove_emp.html',context)



def filter_emp(request):
    if request.method=='POST':
        name=request.POST['Name']
        phone_number=request.POST['phone_number']
        role=request.POST['role']
        department=request.POST['department']
        emps=Employes.objects.all()
        if name:
            emps=emps.filter(Q(Name__icontains=name)|Q(last_name__icontains=name))
        if department:
            emps=emps.filter(dept__name__icontains=department)
        if role:
            emps=emps.filter(role__name__icontains=role)
        if phone_number:
            emps=emps.filter(phone_number=phone_number)

        context={
        'emps':emps
         }
        print(context)
        return render(request,'all_emp.html',context)
        
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    
    else:
        return HttpResponse("An Exception Occured")

    