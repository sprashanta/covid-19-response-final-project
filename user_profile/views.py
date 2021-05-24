from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import *
from datetime import datetime
import datetime
from .filters import *
from SuperAdmin.forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
User = get_user_model()


def oxygen_cylinder(request):
    hospital_oxygen_cylinder = OxygenCylinder.objects.all().order_by('-created')
    MyFilter = HospitalLocationFilters(request.GET, queryset=hospital_oxygen_cylinder)
    hospital_oxygen_cylinder = MyFilter.qs
    context = {
        'hospital_oxygen_cylinder': hospital_oxygen_cylinder,
        'MyFilter': MyFilter
    }
    return render(request, 'oxygen_cylinder.html', context=context)


def icu_bed(request):
    hospital_icu_bed = IcuBed.objects.all().order_by('-created')
    MyFilter = HospitalLocationFilters(request.GET, queryset=hospital_icu_bed)
    hospital_icu_bed = MyFilter.qs
    context = {
        'hospital_icu_bed': hospital_icu_bed,
        'MyFilter': MyFilter
    }
    return render(request, 'icu_bed.html', context=context)


def base(request):
    # date_today = datetime.now()
    hospital_icu_bed = IcuBed.objects.all().order_by('-created')[0:3]
    hospital_oxygen_cylinder = OxygenCylinder.objects.all().order_by('-created')[0:3]
    plasma_donor = Plasma.objects.all().order_by('-created')[0:5]

    context = {
        # 'date_today': date_today,
        'hospital_icu_bed': hospital_icu_bed,
        'hospital_oxygen_cylinder': hospital_oxygen_cylinder,
        'plasma_donor': plasma_donor,
    }
    return render(request, 'index.html', context=context)


def plasma_donor(request):
    plasma_donor = Plasma.objects.all()
    MyFilter = PlasmaDonorFilters(request.GET, queryset=plasma_donor)
    plasma_donor = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(plasma_donor, 10)
    try:
        plasma_donor = paginator.page(page)
    except PageNotAnInteger:
        plasma_donor = paginator.page(1)
    except EmptyPage:
        plasma_donor = paginator.page(paginator.num_pages)
    context = {
        'plasma_donor': plasma_donor,
        'MyFilter': MyFilter
    }
    return render(request, 'plasma_donor.html', context=context)


def login(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = User.objects.filter(phone_number=phone_number)
        if user.exists():
            username = user[0].username
            user_authentication = authenticate(request, username=username, password=password)
            print(user_authentication)
            if user_authentication is not None:
                auth_login(request, user_authentication)
                if user_authentication.is_superuser:
                    return redirect(reverse('SuperAdminHome'))
                else:
                    return redirect(reverse('home'))
            else:
                message = "Your Phone Number And Password Is Wrong"
                context = {
                    'message': message,
                }
                return render(request, 'login.html', context=context)
        else:
            message = "Your Phone Number And Password Is Wrong"
            context = {
                'message': message,
            }
            return render(request, 'login.html', context=context)
    if request.method == "GET":
        return render(request, 'login.html')


def patient_signup(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'register.html', context=context)


def after_registration(request):
    return render(request, 'after_registration.html')


# @login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))


def donor_signup(request):
    form = DonorRegistrationForm()
    if request.method == "POST":
        form = DonorRegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'donor_register.html', context=context)


def donor_password_change(request):
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
    return render(request, 'donor_password_change.html', context=context)


def donor_profile(request):
    if request.method == 'POST':
        u_form = DonorUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('donor_profile')
    else:
        u_form = DonorUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'DonorProfile.html', context=context)


def create_donor_plasma(request):
    form = PlasmaForm()
    if request.method == 'POST':
        form = PlasmaForm(request.POST or None)
        if form.is_valid():
            d = form.save(commit=False)
            d.donor_name = request.user
            d.save()
            return redirect('donor_plasma_list')
    context = {
        'form': form
    }
    return render(request, 'donor_plasma_create.html', context=context)


def donor_plasma_list(request):
    plasma_donor = Plasma.objects.filter(donor_name=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(plasma_donor, 10)
    try:
        plasma_donor = paginator.page(page)
    except PageNotAnInteger:
        plasma_donor = paginator.page(1)
    except EmptyPage:
        plasma_donor = paginator.page(paginator.num_pages)
    context = {
        'plasma_donor': plasma_donor,
    }
    return render(request, 'my_pasma_donor_list.html', context=context)


def donor_plasma_update(request, donor_id):
    donor = Plasma.objects.get(id=donor_id)
    form = PlasmaForm(instance=donor)
    if request.method == 'POST':
        form = PlasmaForm(request.POST or None, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_plasma_list')
    context = {
        'form': form
    }
    return render(request, 'donor_plasma_update.html', context=context)
