import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
import time
from .models import Timer
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
# contains = f"{datetime.datetime.now().year}-0{datetime.datetime.now().month}-{datetime.datetime.now().day}"
contains = str(datetime.datetime.now()).split(" ")[0]


@login_required
def home(request):
    return render(request, 'time_app/home.html')


@login_required
def start_work(request):
    starting_time = datetime.datetime.now()# .strftime('%d/%m/%y %H:%M:%S')
    if not Timer.objects.all().filter(user=request.user, start_work__contains=contains):
        Timer.objects.create(user=request.user, start_work=starting_time)
    else:
        messages.error(request, "You cant press that button, today try tomorrow")

    # starting_time = timezone.now()
    print(starting_time)

    # Timer.objects.create(user=request.user, start_work=starting_time)
    print('######################################################################')
    # print(Timer.objects.all().filter(user=request.user))
    print('########################## ############################################')
    return redirect('home_page')


@login_required
def start_break(request):
    break_time_start = datetime.datetime.now()# .strftime('%d/%m/%y %H:%M:%S')
    Timer.objects.filter(user=request.user, start_work__startswith=contains).update(start_break=break_time_start)
    return redirect('home_page')


@login_required
def end_break(request):
    break_time_end = datetime.datetime.now()# .strftime('%d/%m/%y %H:%M:%S')
    Timer.objects.filter(user=request.user, start_work__startswith=contains).update(end_break=break_time_end)
    # away = str(Timer.objects.all().filter(user=request.user).split('|'))[3] - \
    #        str(Timer.objects.all().filter(user=request.user).split('|'))[2]
    # print(away)

    # away = str(Timer.objects.all().filter(user=request.user)).split('|')[3] - str(Timer.objects.all().filter(user=request.user)).split('|')[2]
    # print(str(Timer.objects.all().filter(user=request.user)))
    away = datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user)).split('|')[3], '%d/%m/%y %H:%M:%S') - datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user)).split('|')[2], '%d/%m/%y %H:%M:%S')
    print(away)
    # data = {'id': 'id', 'start_work': 'start_work', 'start_break': 'start_break',
    #         'end_break': 'end_break', 'end_work': 'end_work', 'away': 'away', 'actually_worked_hours': 'actually_worked_hours',
    #         'user': 'user_id'}
    # Timer.objects.raw('SELECT * FROM time_app_timer', translations=data)

    # data = Timer.objects.raw('SELECT start_break, end_break FROM time_app_timer')
    #
    #
    # print(data)

    # print(a.split("|")[])
    # print(type(a))
    return redirect('home_page')


@login_required
def end_work(request):
    end_time = datetime.datetime.now()# .strftime('%d/%m/%y %H:%M:%S')

    if not Timer.objects.all().filter(user=request.user, end_work__contains=contains):
        Timer.objects.all().filter(user=request.user, start_work__startswith=contains).update(end_work=end_time)

    print('######################################################################')
    # print(workday)
    # print(str(end_time), type(end_time))
    #3 print(workday)
    # print(Timer.objects.all().filter(user=request.user, start_work__startswith='2021-06-15'))
    print('######################################################################')
    # Timer.objects.update(user=request.user, end_work=end_time)
    # Timer.objects.update(user=request.user, start_work=workday, end_work=end_time)
    return redirect('home_page')
    a = Timer.objects.raw('select end_break from time_app_timer')
    print(a)

def actually_worked_hours(request):
    print("Actually worked hours")
    for i in Timer.objects.all():
        print(i)
        print(str(i).split('|'))
    return HttpResponse("test")

