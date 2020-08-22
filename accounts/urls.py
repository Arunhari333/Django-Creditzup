from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

app_name = 'accounts'

urlpatterns = [
    path('', views.home),
    path('national-initiatives', views.national_initiatives.as_view(), name='natpage'),
    path('sports-&-games', views.sports_games.as_view(), name='gamepage'),
    path('cultural-activities', views.cultural_activities.as_view(), name='cultpage'),
    path('prof-self-initiatives', views.prof_self_initiatives.as_view(), name='profpage'),
    path('entrepreneurship-&-innovation', views.Entrepreneurship_innovation.as_view(), name='entrepage'),
    path('leadership-&-management', views.Leadership_management.as_view(), name='leadpage'),
    path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('uploads/', views.uploads, name='uploads'),
    path('national-initiatives/view/<int:id>/', views.view_natpage, name='view_natpage'),
    path('sports-&-games/view/<int:id>/', views.view_gamepage, name='view_gamepage'),
    path('cultural-activities/view/<int:id>/', views.view_cultpage, name='view_cultpage'),
    path('prof-self-initiatives/view/<int:id>/', views.view_profpage, name='view_profpage'),
    path('entrepreneurship-&-innovation/view/<int:id>/', views.view_entrepage, name='view_entrepage'),
    path('leadership-&-management/view/<int:id>/', views.view_leadpage, name='view_leadpage'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('national-initiatives/edit/<int:id>/', views.edit_natpage, name='edit_natpage'),
    path('sports-&-games/edit/<int:id>/', views.edit_gamepage, name='edit_gamepage'),
    path('cultural-activities/edit/<int:id>/', views.edit_cultpage, name='edit_cultpage'),
    path('prof-self-initiatives/edit/<int:id>/', views.edit_profpage, name='edit_profpage'),
    path('entrepreneurship-&-innovation/edit/<int:id>/', views.edit_entrepage, name='edit_entrepage'),
    path('leadership-&-management/edit/<int:id>/', views.edit_leadpage, name='edit_leadpage'),
    path('national-initiatives/delete/<int:id>/', views.delete_natpage, name='delete_natpage'),
    path('sports-&-games/delete/<int:id>/', views.delete_gamepage, name='delete_gamepage'),
    path('cultural-activities/delete/<int:id>/', views.delete_cultpage, name='delete_cultpage'),
    path('prof-self-initiatives/delete/<int:id>/', views.delete_profpage, name='delete_profpage'),
    path('entrepreneurship-&-innovation/delete/<int:id>/', views.delete_entrepage, name='delete_entrepage'),
    path('leadership-&-management/delete/<int:id>/', views.delete_leadpage, name='delete_leadpage'),
    path('change-password', views.change_password, name='change_password'),
    path('reset-password', PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView,
         {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    path('reset-password/confirm/[?P<uidb64>[0-9A-Za-z]+]-(?P<token>.+)',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
