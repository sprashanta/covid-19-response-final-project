from django.shortcuts import render, redirect, reverse
from .forms import *
from patient.models import MakeAppointment
from user_profile.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def doctor_profile(request):
    if request.method == 'POST':
        u_form = DoctorUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('doctor_profile')
    else:
        u_form = DoctorUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Doctor/DoctorProfile.html', context=context)


def doctor_view_appointment(request):
    user = User.objects.get(username=request.user)
    appointment = MakeAppointment.objects.filter(doctor_name=user)
    context = {
        'appointment': appointment
    }
    return render(request, 'Doctor/view_appointment_list.html', context=context)


def update_checkup_status(request, pk):
    checkup = MakeAppointment.objects.get(pk=pk)
    if request.method == "POST":
        form = DoctorChangeCheckUpForm(request.POST or None, instance=checkup)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor_view_appointment'))
        context = {
            'form': form
        }
        return render(request, 'Doctor/doctor_change_checkup_appointment_status.html', context=context)
    if request.method == "GET":
        form = DoctorChangeCheckUpForm(instance=checkup)
        context = {
            'form': form
        }
        return render(request, 'Doctor/doctor_change_checkup_appointment_status.html', context=context)


def doctor_password_change(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
        context = {
            'form': form
        }
    return render(request, 'doctor_password_change.html', context=context)
