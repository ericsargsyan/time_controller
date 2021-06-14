import datetime

from django.shortcuts import render, redirect
import time
from .models import Timer
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    start_work = time.time()
    time.sleep(65)
    end_work = time.time()
    total = round((end_work - start_work) / 60, 2)
    print(total)
    return render(request, 'time_app/home.html')


def start_work(request):
    # if request.Method == 'POST':
    #     pass
    starting_time = datetime.datetime.now()
    # starting_time = timezone.now()
    print(starting_time)
    Timer.objects.create(user=request.user, start_work=starting_time)
    return redirect('home_page')


def end_work(request):
    end_time = datetime.datetime.now()
    workday = Timer.objects.all().filter(user=request.user, start_work__contains=f"{datetime.datetime.now().year}-"
                                                                       f"{datetime.datetime.now().month}-"
                                                                       f"{datetime.datetime.now().day}")
    Timer.objects.update(user=request.user, end_work=end_time)
    return redirect('home_page')



