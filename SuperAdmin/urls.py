from django.urls import path

from SuperAdmin import views

urlpatterns = [
    path('', views.dashboard, name='SuperAdminHome'),

    path('degree/list/', views.list_degree, name='list_degree'),
    path('degree/create/', views.create_degree, name='create_degree'),
    path('degree/update/<int:pk>/', views.update_degree, name='update_degree'),
    path('degree/delete/<int:pk>/', views.delete_degree, name='delete_degree'),

    path('specialist/list/', views.list_specialist, name='list_specialist'),
    path('specialist/create/', views.create_specialist, name='create_specialist'),
    path('specialist/update/<int:pk>/', views.update_specialist, name='update_specialist'),
    path('specialist/delete/<int:pk>/', views.delete_specialist, name='delete_specialist'),

    path('hospital/list/', views.list_hospital, name='list_hospital'),
    path('hospital/create/', views.create_hospital, name='create_hospital'),
    path('hospital/update/<int:pk>/', views.update_hospital, name='update_hospital'),
    path('hospital/delete/<int:pk>/', views.delete_hospital, name='delete_hospital'),

    path('doctor/list/', views.list_doctor, name='list_doctor'),
    path('doctor/create/', views.create_doctor, name='create_doctor'),
    path('doctor/view/<int:pk>/', views.view_doctor, name='view_doctor'),
    path('doctor/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),

    path('icu/list/', views.list_icu_bed_number, name='list_icu'),
    path('icu/create/', views.create_icu_bed_number, name='create_icu'),
    path('icu/update/<int:pk>/', views.update_icu_bed_number, name='update_icu'),
    path('icu/delete/<int:pk>/', views.delete_icu_bed_number, name='delete_icu'),

    path('oxygen/list/', views.list_oxygen_cylinder_number, name='list_oxygen'),
    path('oxygen/create/', views.create_oxygen_cylinder_number, name='create_oxygen'),
    path('oxygen/update/<int:pk>/', views.update_oxygen_cylinder_number, name='update_oxygen'),
    path('oxygen/delete/<int:pk>/', views.delete_oxygen_cylinder_number, name='delete_oxygen'),

    path('plasma/list/', views.list_plasma, name='list_plasma'),
    path('plasma/create/', views.create_plasma, name='create_plasma'),
    path('plasma/view/<int:pk>/', views.view_plasma, name='view_plasma'),
    path('plasma/delete/<int:pk>/', views.delete_plasma, name='delete_plasma'),

    path('location/list/', views.list_location, name='list_location'),
    path('location/create/', views.create_location, name='create_location'),
    path('location/update/<int:pk>/', views.update_location, name='update_location'),
    path('location/delete/<int:pk>/', views.delete_location, name='delete_location'),

    path('super_admin_profile/', views.super_admin_profile, name='super_admin_profile'),

    path('admin_view_appointment/', views.admin_view_appointment, name='admin_view_appointment'),
    path('admin_appointment_update/<int:pk>/', views.admin_appointment_update, name='admin_appointment_update'),
    path('admin_appointment_delete/<int:pk>/', views.admin_appointment_delete, name='admin_appointment_delete'),

    path('admin_view_vaccine_apply/', views.admin_view_vaccine_apply, name='admin_view_vaccine_apply'),
    path('admin_vaccine_delete/<int:pk>/', views.admin_vaccine_delete, name='admin_vaccine_delete'),
    path('admin_vaccine_update/<int:pk>/', views.admin_vaccine_update, name='admin_vaccine_update'),

    path('icu_booking_list/', views.icu_booking_list, name='icu_booking_list'),
    path('icu_booking_delete/<int:pk>/', views.icu_booking_delete, name='icu_booking_delete'),
    path('icu_booking_status_change/<int:pk>/', views.icu_booking_status_change, name='icu_booking_status_change'),

    path('oxygen_cylinder_booking_list/', views.oxygen_cylinder_booking_list, name='oxygen_cylinder_booking_list'),
    path('oxygen_cylinder_booking_status_change/<int:pk>/', views.oxygen_cylinder_booking_status_change,
         name='oxygen_cylinder_booking_status_change'),

    path('password_change/', views.password_change, name='super_admin_password_change'),

]
