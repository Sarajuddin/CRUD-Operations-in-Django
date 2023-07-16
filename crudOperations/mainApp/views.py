from django.shortcuts import render, redirect
from mainApp.models import Record
from django.db.models import Q

# Create your views here.
def home(request):
    data = Record.objects.all()
    return render(request, 'home.html', {'data':data})

def add(request):
    if request.method=='POST':
        info = Record()
        info.name = request.POST.get('name')
        info.email = request.POST.get('email')
        info.mobile = request.POST.get('mobile')
        info.city = request.POST.get('city')
        info.state = request.POST.get('state')
        info.pincode = request.POST.get('pincode')
        info.save()
        return redirect("/")
        
    return render(request, 'add.html')

def delete(request, userId):
    info = Record.objects.get(id=userId)
    info.delete()
    return redirect('/')

def update(request, userId):
    if request.method=='POST':
        info = Record()
        info.id = userId
        info.name = request.POST.get('name')
        info.email = request.POST.get('email')
        info.mobile = request.POST.get('mobile')
        info.city = request.POST.get('city')
        info.state = request.POST.get('state')
        info.pincode = request.POST.get('pincode')
        info.save()
        return redirect("/")

    info = Record.objects.get(id=userId)
    return render(request, 'update.html', {'info':info})

def search(request):
    if request.method=='POST':
        query = request.POST.get('search')
        data = Record.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(mobile__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(pincode__icontains=query))
        
        return render(request, 'home.html', {'data':data})
    else:
        return redirect('/')