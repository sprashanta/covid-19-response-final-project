from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import *
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
User = get_user_model()


def dashboard(request):
    return render(request, 'SuperAdmin/SuperAdminNavbar.html')


def list_degree(request):
    degree = Degree.objects.all()
    context = {
        'degree': degree
    }
    return render(request, 'SuperAdmin/Degree/degree_list.html', context=context)


def create_degree(request):
    form = DegreeForm()
    if request.method == 'POST':
        form = DegreeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_degree')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Degree/degree_create.html', context=context)


def update_degree(request, pk):
    degree = get_object_or_404(Degree, pk=pk)
    form = DegreeForm(instance=degree)
    if request.method == 'POST':
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            form.save()
            return redirect('list_degree')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Degree/degree_update.html', context=context)


def delete_degree(request, pk):
    degree = get_object_or_404(Degree, pk=pk)
    if request.method == 'POST':
        degree.delete()
        return redirect('list_degree')
    context = {
        'degree': degree
    }
    return render(request, 'SuperAdmin/Degree/degree_delete.html', context)


def list_location(request):
    location = Location.objects.all()
    context = {
        'location': location
    }
    return render(request, 'SuperAdmin/Location/location_list.html', context=context)


def create_location(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_location')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Location/location_create.html', context=context)


def update_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    form = LocationForm(instance=location)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('list_location')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Location/location_update.html', context=context)


def delete_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('list_location')
    context = {
        'location': location
    }
    return render(request, 'SuperAdmin/Location/location_delete.html', context)


def list_specialist(request):
    specialist = Specialist.objects.all()
    context = {
        'specialist': specialist
    }
    return render(request, 'SuperAdmin/Specialist/specialist_list.html', context=context)


def create_specialist(request):
    form = SpecialistForm()
    if request.method == 'POST':
        form = SpecialistForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_specialist')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Specialist/specialist_create.html', context=context)


def update_specialist(request, pk):
    specialist = get_object_or_404(Specialist, pk=pk)
    form = SpecialistForm(instance=specialist)
    if request.method == 'POST':
        form = SpecialistForm(request.POST, instance=specialist)
        if form.is_valid():
            form.save()
            return redirect('list_specialist')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Specialist/specialist_update.html', context=context)


def delete_specialist(request, pk):
    specialist = get_object_or_404(Specialist, pk=pk)
    if request.method == 'POST':
        specialist.delete()
        return redirect('list_specialist')
    context = {
        'specialist': specialist
    }
    return render(request, 'SuperAdmin/Specialist/specialist_delete.html', context)


def list_hospital(request):
    hospital = Hospital.objects.all()
    context = {
        'hospital': hospital
    }
    return render(request, 'SuperAdmin/Hospital/hospital_list.html', context=context)


def create_hospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_hospital')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Hospital/hospital_create.html', context=context)


def update_hospital(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    form = HospitalForm(instance=hospital)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('list_hospital')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Hospital/hospital_update.html', context=context)


def delete_hospital(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.delete()
        return redirect('list_hospital')
    context = {
        'hospital': hospital
    }
    return render(request, 'SuperAdmin/Hospital/hospital_delete.html', context)


def list_doctor(request):
    doctor = User.objects.filter(is_doctor=True)
    context = {
        'doctor': doctor
    }
    return render(request, 'SuperAdmin/Doctor/doctor_list.html', context=context)


def create_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            d = form.save(commit=False)
            d.is_doctor = True
            d.save()
            return redirect('list_doctor')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Doctor/doctor_create.html', context=context)


def view_doctor(request, pk):
    doctor = get_object_or_404(User, pk=pk)
    context = {
        'doctor': doctor
    }
    return render(request, 'SuperAdmin/Doctor/doctor_view.html', context=context)


def delete_doctor(request, pk):
    doctor = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctor')
    context = {
        'doctor': doctor
    }
    return render(request, 'SuperAdmin/Doctor/doctor_delete.html', context=context)


def list_icu_bed_number(request):
    icu = IcuBed.objects.all()
    context = {
        'icu': icu
    }
    return render(request, 'SuperAdmin/ICU/icu_list.html', context=context)


def create_icu_bed_number(request):
    form = IcuBedForm()
    if request.method == 'POST':
        form = IcuBedForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_icu')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/ICU/icu_create.html', context=context)


def update_icu_bed_number(request, pk):
    icu = get_object_or_404(IcuBed, pk=pk)
    form = IcuBedUpdateForm(instance=icu)
    if request.method == 'POST':
        form = IcuBedUpdateForm(request.POST, instance=icu)
        if form.is_valid():
            form.save()
            return redirect('list_icu')
    context = {
        'form': form,
        'icu': icu
    }
    return render(request, 'SuperAdmin/ICU/icu_update.html', context=context)


def delete_icu_bed_number(request, pk):
    icu = get_object_or_404(IcuBed, pk=pk)
    if request.method == 'POST':
        icu.delete()
        return redirect('list_icu')
    context = {
        'icu': icu
    }
    return render(request, 'SuperAdmin/ICU/icu_delete.html', context=context)


def list_oxygen_cylinder_number(request):
    oxygen = OxygenCylinder.objects.all()
    context = {
        'oxygen': oxygen
    }
    return render(request, 'SuperAdmin/OxygenCylinder/oxygen_cylinder_list.html', context=context)


def create_oxygen_cylinder_number(request):
    form = OxygenCylinderForm()
    if request.method == 'POST':
        form = OxygenCylinderForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_oxygen')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/OxygenCylinder/oxygen_cylinder_create.html', context=context)


def update_oxygen_cylinder_number(request, pk):
    oxygen = get_object_or_404(OxygenCylinder, pk=pk)
    form = OxygenCylinderForm(instance=oxygen)
    if request.method == 'POST':
        form = OxygenCylinderForm(request.POST, instance=oxygen)
        if form.is_valid():
            form.save()
            return redirect('list_oxygen')
    context = {
        'form': form,
        'oxygen': oxygen
    }
    return render(request, 'SuperAdmin/OxygenCylinder/oxygen_cylinder_update.html', context=context)


def delete_oxygen_cylinder_number(request, pk):
    oxygen = get_object_or_404(OxygenCylinder, pk=pk)
    if request.method == 'POST':
        oxygen.delete()
        return redirect('list_oxygen')
    context = {
        'oxygen': oxygen
    }
    return render(request, 'SuperAdmin/OxygenCylinder/oxygen_cylinder_delete.html', context=context)


def super_admin_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('super_admin_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'SuperAdmin/Profile/SuperAdminProfile.html', context=context)


def list_plasma(request):
    plasma = Plasma.objects.all()
    context = {
        'plasma': plasma
    }
    return render(request, 'SuperAdmin/Plasma/plasma_list.html', context=context)


def create_plasma(request):
    form = PlasmaForm()
    if request.method == 'POST':
        form = PlasmaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_plasma')
    context = {
        'form': form
    }
    return render(request, 'SuperAdmin/Plasma/plasma_create.html', context=context)


def view_plasma(request, pk):
    plasma = get_object_or_404(Plasma, pk=pk)
    context = {
        'plasma': plasma
    }
    return render(request, 'SuperAdmin/Plasma/plasma_view.html', context=context)


def delete_plasma(request, pk):
    plasma = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        plasma.delete()
        return redirect('list_plasma')
    context = {
        'plasma': plasma
    }
    return render(request, 'SuperAdmin/Plasma/plasma_delete.html', context=context)


def admin_view_appointment(request):
    appointment = MakeAppointment.objects.all()
    context = {
        'appointment': appointment
    }
    return render(request, 'SuperAdmin/Appointment/appointment_list.html', context=context)


def admin_appointment_update(request, pk):
    appointment = MakeAppointment.objects.get(pk=pk)
    form = UpdateMakeAppointmentForm(instance=appointment)
    if request.method == "POST":
        form = UpdateMakeAppointmentForm(request.POST or None, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_view_appointment'))
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/Appointment/appointment_update.html', context=context)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/Appointment/appointment_update.html', context=context)


def admin_appointment_delete(request, pk):
    appointment = MakeAppointment.objects.get(pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('admin_view_appointment')
    context = {
        'appointment': appointment
    }
    return render(request, 'SuperAdmin/Appointment/appointment_delete.html', context=context)


def admin_view_vaccine_apply(request):
    vaccine = Vaccine.objects.all()
    context = {
        'vaccine': vaccine
    }
    return render(request, 'SuperAdmin/Vaccine/vaccine_list.html', context=context)


def admin_vaccine_delete(request, pk):
    vaccine = Vaccine.objects.get(pk=pk)
    if request.method == 'POST':
        vaccine.delete()
        return redirect('admin_view_vaccine_apply')
    context = {
        'vaccine': vaccine
    }
    return render(request, 'SuperAdmin/Vaccine/vaccine_delete.html', context=context)


def admin_vaccine_update(request, pk):
    vaccine = Vaccine.objects.get(pk=pk)
    form = UpdatePatientVaccine(instance=vaccine)
    if request.method == "POST":
        form = UpdatePatientVaccine(request.POST or None, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_view_vaccine_apply'))
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/Vaccine/vaccine_update.html', context=context)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/Vaccine/vaccine_update.html', context=context)


def icu_booking_list(request):
    booking_icu_bed = IcuBedBooking.objects.all()
    context = {
        'booking_icu_bed': booking_icu_bed
    }
    return render(request, 'SuperAdmin/IcuBooking/booking_icu_bed.html', context=context)


def icu_booking_status_change(request, pk):
    booking_icu_bed = IcuBedBooking.objects.get(pk=pk)
    print('booking ', booking_icu_bed)
    form = IcuBedBookingStatusChange(instance=booking_icu_bed)
    if request.method == "POST":
        form = IcuBedBookingStatusChange(request.POST or None, instance=booking_icu_bed)
        if form.is_valid():
            bib = form.save(commit=False)
            hospital_name = booking_icu_bed.hospital_name
            print(hospital_name)
            status = form.cleaned_data.get('status')

            if status == "Approved":

                icu_bed_inverse = IcuBed.objects.get(hospital=hospital_name)
                icu_bed_inverse.icu_bed_number -= 1
                icu_bed_inverse.save()
                bib.save()
                return redirect(reverse('icu_booking_list'))
            if status == "Decline":
                bib.save()
                return redirect(reverse('icu_booking_list'))
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/IcuBooking/booking_icu_bed_status_change.html', context=context)


def icu_booking_delete(request, pk):
    booking_icu_bed = IcuBedBooking.objects.get(pk=pk)
    if request.method == 'POST':
        booking_icu_bed.delete()
        return redirect(reverse('icu_booking_list'))
    context = {
        'booking_icu_bed': booking_icu_bed
    }
    return render(request, 'SuperAdmin/IcuBooking/booking_icu_bed_delete.html', context=context)


def oxygen_cylinder_booking_list(request):
    booking_oxygen_cylinder = OxygenCylinderBooking.objects.all()
    context = {
        'booking_oxygen_cylinder': booking_oxygen_cylinder
    }
    return render(request, 'SuperAdmin/OxygenCylinderBooking/booking_oxygen_cylinder.html', context=context)


def oxygen_cylinder_booking_status_change(request, pk):
    booking_oxygen_cylinder = OxygenCylinderBooking.objects.get(pk=pk)
    form = OxygenCylinderBookingStatusChange(instance=booking_oxygen_cylinder)
    if request.method == "POST":
        form = OxygenCylinderBookingStatusChange(request.POST or None, instance=booking_oxygen_cylinder)
        if form.is_valid():
            ocb = form.save(commit=False)
            hospital_name = form.cleaned_data.get('hospital_name')
            status = form.cleaned_data.get('status')
            if status == "Approved":
                oxygen_cylinder_inverse = OxygenCylinder.objects.get(hospital=hospital_name)
                oxygen_cylinder_inverse.oxygen_cylinder_number -= 1
                oxygen_cylinder_inverse.save()
                ocb.save()
            return redirect(reverse('oxygen_cylinder_booking_list'))
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/OxygenCylinderBooking/booking_oxygen_cylinder_status_change.html',
                      context=context)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'SuperAdmin/OxygenCylinderBooking/booking_oxygen_cylinder_status_change.html',
                      context=context)


def password_change(request):
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
    return render(request, 'SuperAdmin/password_change.html', context=context)
