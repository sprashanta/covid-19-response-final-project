from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base, name='home'),
    path('login/', login, name='login'),
    path('patient_signup/', patient_signup, name='patient_signup'),
    path('donor_password_change/', donor_password_change, name='donor_password_change'),
    path('donor_profile/', donor_profile, name='donor_profile'),
    path('create_donor_plasma/', create_donor_plasma, name='create_donor_plasma'),
    path('donor_plasma_update/<int:donor_id>/', donor_plasma_update, name='donor_plasma_update'),
    path('donor_plasma_list/', donor_plasma_list, name='donor_plasma_list'),

    path('donor_signup/', donor_signup, name='donor_signup'),
    path('after_registration/', after_registration, name='after_registration'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='password_change_done.html'), name='password_change_done'),

]
