from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from .forms import *

# Create your views here.

def home(request):
    print(models.TrainStops.objects.filter(number_id=2))
    return render(request,"index.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
        
    elif request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required
def search_trains(request):
    
    if request.method=="POST":
        form=SearchTrainForm(request.POST)
        if form.is_valid():
            print(1)
            print(models.TrainStops.objects.all())
            from_station=form.cleaned_data['from_station']
            to_station=form.cleaned_data['to_station']
            print(from_station)
            date=form.cleaned_data['date']
            seats=form.cleaned_data['seats']
            class_type=form.cleaned_data['class_type']
            trains=[]
            for i in list(models.Train.objects.all()):
                start=False
                start_time=None
                end=False
                end_time=None
                available=0
                for j in list(models.TrainStops.objects.filter(number_id=i).values()):
                    if str(j['stop'])==str(from_station):
                        start=True
                        start_time=j['arrival']
                    elif str(j['stop'])==str(to_station):
                        end_time=j['arrival']
                        end=True
                if start==True and end==True and end_time>start_time:
                    try:
                        available=models.TrainSeats.objects.filter(number_id=int(str(i)),class_type=class_type).values()[0]['available']
                    except:
                        pass
                    print(available)
                    if seats<=available:
                        trains.append(str(i))
            print(trains)
            results=[]
            for i in trains:
                results.append({'number':i,'start':models.TrainStops.objects.filter(number_id=int(i),stop=from_station).values()[0]['arrival'],'end':models.TrainStops.objects.filter(number_id=int(i),stop=to_station).values()[0]['arrival'],'fare':models.TrainSeats.objects.filter(number_id=int(i),class_type=class_type).values()[0]['fare'],'tickets':seats,'class_type':class_type})
            print(results)
            return render(request,'search_trains.html',{'form':form,'trains':results})
    #print(models.TrainStops.objects.values_list('start_stop').distinct())
    form=SearchTrainForm()
    return render(request,'search_trains.html',{'form':form})

def book_tickets(request):
    if request.method=='POST':
        number=request.POST['number']
        seats=request.POST['seats']
        class_type=request.POST['class_type']
        fare=request.POST['fare']
        print("ok",number,seats,class_type,fare)
        if float(fare)>request.user.wallet:
            return HttpResponse("Insufficient Funds!")
        return HttpResponse("Ticket(s) Booked!")
    return redirect('home')

def wallet(request):
    balance=request.user.wallet
    if request.method=="POST":
        form=WalletForm(request.POST)
        if form.is_valid():
            amount=request.POST['amount']
            old_balance=models.CustomUser.objects.get(username=request.user.username)
            old_balance.wallet=balance+float(amount)
            old_balance.save()
            return redirect('wallet')
    form=WalletForm()
    return render(request,'wallet.html',{"balance":balance,'form':form})
