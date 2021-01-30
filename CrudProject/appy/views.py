from django.shortcuts import render, HttpResponseRedirect
from .forms import StdReg
from .models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = StdReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em,password=pw)
            reg.save()
            fm = StdReg()
    else:
        fm = StdReg()
    student = User.objects.all()
    return render(request,'enroll/index.html', {'form':fm,'stu':student })

def update(request):
    return render(request,'enroll/update.html')

def delete_User(request,id=1):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def Update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StdReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            HttpResponseRedirect('../index.html')
    else:
        pi = User.objects.get(pk=id)
        fm = StdReg(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
