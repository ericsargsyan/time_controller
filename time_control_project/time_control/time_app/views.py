import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
import time
from .models import Timer, Break
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
restriction = datetime.datetime.today().strftime('%m/%d/%Y')


@login_required
def home(request):
    return render(request, 'time_app/home.html')


@login_required
def start_work(request):
    starting_time = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.all().filter(user=request.user, start_work__contains=restriction):
        Timer.objects.create(user=request.user, start_work=starting_time)
        messages.success(request, f"Working day started at {starting_time}")
    else:
        messages.error(request, "You cant press that button today, try tomorrow")

    return redirect('home_page')


@login_required
def start_break(request):
    break_time_start = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.filter(user=request.user, end_work__contains=restriction):
           #  and Timer.objects.all().filter(user=request.user, end_break__isnull=True):
        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(start_break=break_time_start, end_break=None)
        messages.success(request, f"Your break started at {break_time_start}")
    else:
        messages.error(request, "Your workday is over!")

    return redirect('home_page')


@login_required
def end_break(request):
    break_time_end = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.filter(user=request.user, end_work__contains=restriction):
           # and Timer.objects.all().filter(user=request.user, start_break__isnull=True):
        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(end_break=break_time_end)
        messages.success(request, "Your break is over!")
        Break.objects.create(user=request.user, start_break=str(Timer.objects.filter(user=request.user, start_work__startswith=restriction)).split('|')[2], end_break=break_time_end)

        away = float(str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[5].split('>')[0])

        t1 = str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[3]
        t2 = str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[2]

        a = datetime.datetime.strptime(t1, '%m/%d/%Y, %H:%M:%S')
        b = datetime.datetime.strptime(t2, '%m/%d/%Y, %H:%M:%S')

        away += ((a - b).total_seconds()) / 60

        Timer.objects.all().filter(user=request.user, start_work__startswith=restriction).update(away=away)
    else:
        messages.error(request, "Your workday is over!")

    return redirect('home_page')


@login_required
def end_work(request):
    end_time = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.all().filter(user=request.user, end_work__contains=restriction):
        Timer.objects.all().filter(user=request.user, start_work__startswith=restriction).update(end_work=end_time)
        messages.success(request, "Your workday is over!")

        start = str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[1]
        finish = str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[4]

        workday = (datetime.datetime.strptime(finish, '%m/%d/%Y, %H:%M:%S') - datetime.datetime.strptime(start, '%m/%d/%Y, %H:%M:%S')).total_seconds() / 3600
        away = float(str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[5].split('>')[0]) / 60

        actual_worked_hours = workday - away

        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(actual_worked_hours=actual_worked_hours)
    else:
        messages.error(request, "You cant press that button now, try later")

    return redirect('home_page')

# datetime.datetime.strptime("07/11/2021, 14:23:14", '%m/%d/%Y, %H:%M:%S')
