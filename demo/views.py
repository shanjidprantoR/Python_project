from django.shortcuts import render,HttpResponse

# Create your views here.
def landing_view(request):
    return render(request,'landing.html')
def home_view(request):
    return render(request,'home.html')
def contact(request):

    return render(request,'contact.html')
def developer(request):
    return render(request,'developer.html')
def profile(request):
    return render(request,'profile.html')
def notification(request):
    return render(request,'notification.html')
def language(request):
    return render(request,'language.html')
def settings(request):
    return render(request,'settings.html')
def more(request):
    return render(request,'more.html')
def firRegistration(request):
    return render(request,'firRegistration.html')
def showupdate(request):
    return render(request,'showupdate.html')
def addinfo(request):
    return render(request,'addinfo.html')
def crimeRecord (request):
    return render(request,'crimeRecord.html')
def emergencyContact (request):
    return render(request,'emergencyContact.html')
def policeStation (request):
    return render(request,'policeStation.html')
def hospital (request):
    return render(request,'hospital.html')
def fireService (request):
    return render(request,'fireService.html')
def login (request):
    return render(request,'login.html')
def signup (request):
    return render(request,'signup.html')
def about (request):
    return render(request,'about.html')
def instructor (request):
    return render(request,'instructor.html')
