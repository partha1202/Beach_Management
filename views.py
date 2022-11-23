from django.shortcuts import render
from beach_management.models import EmpModel
from django.contrib import messages
from beach_management.forms import Empforms

def home(request):
    showall=EmpModel.objects.all()
    return render(request,'home.html',{"data":showall}) 

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall}) 

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('customer_id') and request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('last_name') and request.POST.get('street') and request.POST.get('pincode') and request.POST.get('age') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('membership_card'):
            saverecord=EmpModel()
            saverecord.customer_id=request.POST.get('customer_id')
            saverecord.first_name=request.POST.get('first_name')
            saverecord.middle_name=request.POST.get('middle_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.street=request.POST.get('street')
            saverecord.pincode=request.POST.get('pincode')
            saverecord.age=request.POST.get('age')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.membership_card=(request.POST.get('membership_card')=='true')
            saverecord.save()
            messages.success(request,'Customer ' + saverecord.first_name + ' is Saved Successfully..!') 
            return render(request,'insert.html')
    else :
            return render(request,'insert.html')

def editemp(request,customer_id):
    editempobj=EmpModel.objects.get(customer_id=customer_id)
    return render(request,'edit.html',{"EmpModel":editempobj})

def updateemp(request,customer_id):
    Updateemp=EmpModel.objects.get(customer_id=customer_id)
    form=Empforms(request.POST,instance=Updateemp)
    form['membership_card'].initial = (form['membership_card'].value() == 'True')
    # print(form.data.values)
    if form.is_valid():
        # print('hello form is valid')
        form.save()
        messages.success(request,'Customer record Updated Successfully..!') 

        # messages.success(request,'Record Updated Successfully..!')
        return render(request,'edit.html',{"EmpModel":Updateemp})

def Delemp(request,id):
    delemployee=EmpModel.objects.get(customer_id=id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,"index.html",{"data":showdata})


def sortemp(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=EmpModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortemp.html',context)
    else:
        return render(request,'sortemp.html')
