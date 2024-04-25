from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Cycle,Cooler,FoodPlace,Visit_place
# Create your views here.
def Home(request):
    return render(request,'index.html')
def Cyclepage(request):
    if request.method == "POST":
        Name=request.POST['Name']
        Registration_num = request.POST['reginumber']
        Roll_num = request.POST['rollnumber']
        Hostel = request.POST['hostel']
        Room_number = request.POST['roomnumber']
        Phone_num = request.POST['contactnumber']
        Course = request.POST['course']
        Photo = request.FILES['photo']
        cycledata=Cycle( Name= Name,Registration_num=Registration_num,Roll_num=Roll_num,Hostel=Hostel,Room_number= Room_number,Phone_num=Phone_num,Course=Course,Photo=Photo)
        cycledata.save()
        messages.success(request,'Your Data is saved and it\'s now visible to others in the Buy Now Section!!!')
    return render(request,'cycle.html')

def displayCycle(request):
    cycles=Cycle.objects.all()
    context={'cycle':cycles}
    return render(request,'displaycycle.html',context)

def Coolerpage(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Registration_num = request.POST['reginumber']
        Roll_num = request.POST['rollnumber']
        Hostel = request.POST['hostel']
        Room_number = request.POST['roomnumber']
        Phone_num = request.POST['contactnumber']
        Course = request.POST['course']
        Photo = request.FILES['photo']
        coolerdata = Cooler(Name=Name, Registration_num=Registration_num, Roll_num=Roll_num, Hostel=Hostel,Room_number=Room_number, Phone_num=Phone_num, Course=Course, Photo=Photo)
        coolerdata.save()
        messages.success(request, 'Your Data is saved and it\'s now visible to others in the Buy Now Section!!!')
    return render(request, 'cooler.html')

def displayCooler(request):
    cooler=Cooler.objects.all()
    context={'cooler':cooler}
    return render(request,'displaycooler.html',context)

def Food(request):
    if request.method=="POST":
        Name=request.POST['Name']
        address=request.POST['address']
        foodtype=request.POST['foodtype']
        photo=request.FILES['photo']
        fooddata=FoodPlace(Name=Name,address=address,foodtype=foodtype,photo=photo)
        fooddata.save()
        messages.success(request, 'Food Place added!!')
    return displayFood(request)

def displayFood(request):
    foodplace = FoodPlace.objects.all()
    context = {'foodplace': foodplace}
    return render(request, 'displayfood.html', context);

def Places(request):
    return render(request,'places.html')

def Places(request):
    if request.method=="POST":
        Name=request.POST['name']
        Address=request.POST['address']
        Distance=request.POST['distance']
        Mode=request.POST['mode']
        photo=request.FILES['photo']
        placedata=Visit_place(Name=Name,Address=Address,Distance=Distance,Mode=Mode,Photo=photo)
        placedata.save()
        messages.success(request, 'Place added!!')
    return displayPlace(request)

def displayPlace(request):
    visitplace = Visit_place.objects.all()
    context = {'places': visitplace}
    return render(request, 'displayplace.html', context)



