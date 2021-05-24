from django.shortcuts import render, redirect, reverse
from user_profile.forms import *
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def patient_profile(request):
    if request.method == 'POST':
        u_form = PatientUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('patient_profile')
    else:
        u_form = PatientUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Patient/PatientProfile.html', context=context)


@login_required(login_url='login')
def patient_make_appointment(request):
    if request.method == "POST":
        form = MakeAppointmentForm(request.POST or None)
        if form.is_valid():
            pma = form.save(commit=False)
            pma.patient_name = request.user
            pma.save()
            return redirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, 'Patient/make_appointment_create.html', context=context)
    if request.method == "GET":
        form = MakeAppointmentForm()
        context = {
            'form': form
        }
        return render(request, 'Patient/make_appointment_create.html', context=context)


def patient_view_appointment(request):
    user = User.objects.get(username=request.user)
    appointment = MakeAppointment.objects.filter(patient_name=user)
    context = {
        'appointment': appointment
    }
    return render(request, 'Patient/make_appointment_list.html', context=context)


@login_required(login_url='login')
def patient_vaccine_apply(request):
    if request.method == "POST":
        form = PatientVaccineApply(request.POST or None, request.FILES or None)
        if form.is_valid():
            va = form.save(commit=False)
            va.patient_name = request.user
            va.save()
            return redirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, 'Patient/make_vaccine_create.html', context=context)
    if request.method == "GET":
        form = PatientVaccineApply()
        context = {
            'form': form
        }
        return render(request, 'Patient/make_vaccine_create.html', context=context)


def patient_booking_icu_bed(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    current_user = request.user
    icu_booking = IcuBedBooking()
    icu_booking.patient_name = current_user
    icu_booking.hospital_name = hospital
    icu_booking.save()
    return redirect(reverse('home'))


def patient_booking_list(request):
    booking_icu_bed = IcuBedBooking.objects.filter(patient_name=request.user)
    booking_oxygen_cylinder = OxygenCylinderBooking.objects.filter(patient_name=request.user)
    context = {
        'booking_icu_bed': booking_icu_bed,
        'booking_oxygen_cylinder': booking_oxygen_cylinder,
    }
    return render(request, 'Patient/booking_icu_bed.html', context=context)


def patient_booking_oxygen_cylinder(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    current_user = request.user
    oxygen_cylinder_booking = OxygenCylinderBooking()
    oxygen_cylinder_booking.patient_name = current_user
    oxygen_cylinder_booking.hospital_name = hospital
    oxygen_cylinder_booking.save()
    return redirect(reverse('home'))


def patient_password_change(request):
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
    return render(request, 'password_change.html', context=context)
