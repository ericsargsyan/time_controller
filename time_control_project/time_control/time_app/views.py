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
    # print(type(starting_time))
    # print(datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S').split(", ")[0])
    if not Timer.objects.all().filter(user=request.user, start_work__contains=restriction):
        Timer.objects.create(user=request.user, start_work=starting_time)
    else:
        messages.error(request, "You cant press that button today, try tomorrow")

    # starting_time = timezone.now()
    # print(starting_time)
    #
    # # Timer.objects.create(user=request.user, start_work=starting_time)
    # print('######################################################################')
    # # print(Timer.objects.all().filter(user=request.user))
    # print('######################################################################')
    return redirect('home_page')


@login_required
def start_break(request):
    break_time_start = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.filter(user=request.user, end_work__contains=restriction):
           #  and Timer.objects.all().filter(user=request.user, end_break__isnull=True):
        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(start_break=break_time_start)

        print('######################################################################')
        print(break_time_start)
        print('######################################################################')
    else:
        messages.error(request, "Your workday is over!")

    return redirect('home_page')


@login_required
def end_break(request):
    break_time_end = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.filter(user=request.user, end_work__contains=restriction):
           # and Timer.objects.all().filter(user=request.user, start_break__isnull=True):
        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(end_break=break_time_end)
        Break.objects.create(user=request.user, start_break=str(Timer.objects.filter(user=request.user, start_work__startswith=restriction)).split('|')[2], end_break=break_time_end)
        away = float(str(Timer.objects.all().filter(user=request.user)).split('|')[5].split('>')[0])
        # print(type(away))
        print(away)
        print('######################################################################')
        away += (datetime.datetime.strptime(
           str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[3],
           '%m/%d/%Y, %H:%M:%S') - datetime.datetime.strptime(
           str(Timer.objects.all().filter(user=request.user)).split('|')[2],
           '%m/%d/%Y, %H:%M:%S')).total_seconds() / 60
        # print(away)
        # print()
        print('######################################################################')
        print(away)
        Timer.objects.all().filter(user=request.user, start_work__startswith=restriction).update(away=away)

    # Break.objects.all().filter(user=request.user, start_break__startswith="????????").update(end_break=break_time_end)
    else:
        messages.error(request, "Your workday is over!")


    # away = str(Timer.objects.all().filter(user=request.user).split('|'))[3] - \
    #        str(Timer.objects.all().filter(user=request.user).split('|'))[2]
    # print(away)

    # away = str(Timer.objects.all().filter(user=request.user)).split('|')[3] - str(Timer.objects.all().filter(user=request.user)).split('|')[2]
    # print(str(Timer.objects.all().filter(user=request.user)))


    # Timer.objects.all().filter(user=request.user, start_work__startswith=contains).update(away=)


    print("###########################################")
    print("###########################################")
    # away = Timer.objects.raw(f"""select * from time_app_timer where id={request.user.id}""")[0]
   #  # print(away)
   #  # print(str(away).split('|'))
   # #  datetime.datetime.strptime(str(away).split('|')[3], '%m/%d/%Y, %H:%M:%S')
   #  datetime.datetime()
   #  print(str(away).replace('+00:00', ''))
   #  print(str(away).split('|'))
   #  # print(str(away).split('|')[3])
   #  # print(datetime.datetime.strptime(str(away).split('|')[3], '%m/%d/%Y, %H:%M:%S'))
   #  print(str(away).split('|')[3])
    # print(datetime.datetime.strptime(str(away).split('|')[3], '%m/%d/%Y, %H:%M:%S'))
    # 1)
    # away = str(Timer.objects.raw(f"""select * from time_app_timer where id={request.user.id}""")[0]).replace('+00:00', '').split('|')

    # print(type(away[3]))

    # print(away[3].replace(' ', ', '))
   #  print(datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S'))
    # print(datetime.datetime.strptime('06/19/2021, 20:25:30', '%m/%d/%Y, %H:%M:%S'))
    # print(datetime.datetime.strptime(away[3].replace(' ', ', '), '%m/%d/%Y, %H:%M:%S') - datetime.datetime.strptime(away[2].replace(' ', ', '), '%m/%d/%Y, %H:%M:%S'))
    # print(str(away).split('|'))
    # print(away.split('|')[3] - away.split('|')[2])
    print("###########################################")
    print("###########################################")


    # away = datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user)).split('|')[3], '%d/%m/%y %H:%M:%S') - datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user)).split('|')[2], '%d/%m/%y %H:%M:%S')
    # print(away)
    # data = {'id': 'id', 'start_work': 'start_work', 'start_break': 'start_break',
    #           'end_break': 'end_break', 'end_work': 'end_work', 'away': 'away', 'actually_worked_hours': 'actually_worked_hours',
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
    end_time = datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    if not Timer.objects.all().filter(user=request.user, end_work__contains=restriction):
        Timer.objects.all().filter(user=request.user, start_work__startswith=restriction).update(end_work=end_time)

        print('######################################################################')
        # print(workday)
        # print(str(end_time), type(end_time))
        # 3 print(workday)
        # print(Timer.objects.all().filter(user=request.user, start_work__startswith='2021-06-15'))
        print('######################################################################')
        # Timer.objects.update(user=request.user, end_work=end_time)
        # Timer.objects.update(user=request.user, start_work=workday, end_work=end_time)

        # actual_worked_hours = (datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[4], '%m/%d/%Y, %H:%M:%S') - datetime.datetime.strptime(str(Timer.objects.all().filter(user=request.user)).split('|')[1], '%m/%d/%Y, %H:%M:%S')).total_seconds() / 60
        actual_worked_hours = ((datetime.datetime.strptime(
            str(Timer.objects.all().filter(user=request.user, start_work__startswith=restriction)).split('|')[4],
            '%m/%d/%Y, %H:%M:%S') - datetime.datetime.strptime(
            str(Timer.objects.all().filter(user=request.user)).split('|')[1],
            '%m/%d/%Y, %H:%M:%S')).total_seconds() / 60) - float(
            str(Timer.objects.filter(user=request.user, start_work__startswith=restriction)).split('|')[5].split('>')[
                0])
        print(actual_worked_hours)
        Timer.objects.filter(user=request.user, start_work__startswith=restriction).update(
            actual_worked_hours=actual_worked_hours / 60)

    else:
        messages.error(request, "You cant press that button now, try later")

    return redirect('home_page')
