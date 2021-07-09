from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserRegisterForm
from django.contrib import messages
from time_app.models import Timer, Break

# Create your views here


def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User was created successfully!')
            username = form.data.get("username")
            password = form.data.get("password1")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            return redirect("home_page")
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            # p_form.save()
            # messages.success(request, "Your account has been updated successfully!")
            messages.add_message(request, messages.SUCCESS, "Your account has been updated successfully!")
            return redirect('profile_page')

    u_form = UserUpdateForm(instance=request.user)
    # p_form = ProfileUpdateForm(instance=request.user.profile)

    actual_worked_hours = [str(Timer.objects.filter(user=request.user)).split('|')[1].split(',')[0], str(Timer.objects.filter(user=request.user)).split('|')[-1].split('>')[0]]
    print(actual_worked_hours)

    context = {
                'u_form': u_form,
                'actual_worked_hours': actual_worked_hours
                # 'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    return render(request, 'users/logout.html')
