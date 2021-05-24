"""covid_19_response URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user_profile.views import *
from doctor.views import *
from patient.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')),
    path('Super/Admin/', include('SuperAdmin.urls')),

    # user profile
    path('logout/', user_logout, name='logout'),
    path('icu_bed/', icu_bed, name='icu_bed'),
    path('oxygen_cylinder/', oxygen_cylinder, name='oxygen_cylinder'),
    path('plasma_donor/', plasma_donor, name='plasma_donor'),


    # patient
    path('patient_profile/', patient_profile, name='patient_profile'),
    path('patient_password_change/', patient_password_change, name='patient_password_change'),
    path('patient_make_appointment/', patient_make_appointment, name='patient_make_appointment'),
    path('patient_view_appointment/', patient_view_appointment, name='patient_view_appointment'),
    path('patient_vaccine_apply/', patient_vaccine_apply, name='patient_vaccine_apply'),
    path('patient_booking_list/', patient_booking_list, name='patient_booking_list'),
    path('patient_booking_icu_bed/<int:hospital_id>/', patient_booking_icu_bed, name='patient_booking_icu_bed'),
    path('patient_booking_oxygen_cylinder/<int:hospital_id>/', patient_booking_oxygen_cylinder,
         name='patient_booking_oxygen_cylinder'),


    #  doctor
    path('doctor_profile/', doctor_profile, name='doctor_profile'),
    path('doctor_view_appointment/', doctor_view_appointment, name='doctor_view_appointment'),
    path('update_checkup_status/<int:pk>/', update_checkup_status, name='update_checkup_status'),
    path('doctor_password_change/', doctor_password_change, name='doctor_password_change'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
