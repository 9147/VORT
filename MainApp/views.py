from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
from .sign import calculate_file_hash
from .models import *
def home(request):
    return render(request,'MainApp/home.html')

def file_upload_view(request):
    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES['file']
        value=calculate_file_hash(file)
        event = Event.objects.get(name='Avalanche-2023')
        if Certificate.objects.verify_certificate_hash(event,value):
            return JsonResponse({'data':"The certificate is valid! "})
        return JsonResponse({'data':"this certificate is not valid!!"})
    return HttpResponse(status=404)

def loginMe(request):
    return render(request,'MainApp/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("success")
            return JsonResponse({'data':'success'})
        else:
            return HttpResponse(status=401)
    return HttpResponse(status=404)

def logoutPage(request):
    logout(request)
    return home(request)

def addhash(request):
    return render(request,'MainApp/hash.html')

def gethash(request):
    if request.method== 'POST':
        hash = request.POST['hash']
        hash = list(hash.strip().split(','))
        event = Event.objects.get(name='Avalanche-2023')
        for a in hash:
            if a!='':
                val = Certificate(event=event,hash_value=a)
                val.save()
        print(event)
        print(hash)
        return JsonResponse({'data':'success'})
    return HttpResponse(status=404)
