from django.urls import path
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)

urlpatterns = [
    path('', views.home),
    path('national-initiatives', views.national_initiatives.as_view()),
    path('sports-&-games', views.sports_games.as_view()),
    path('cultural-activities', views.cultural_activities.as_view()),
    path('prof-self-initiatives', views.prof_self_initiatives.as_view()),
    path('entrepreneurship-&-innovation', views.Entrepreneurship_innovation.as_view()),
    path('leadership-&-management', views.Leadership_management.as_view()),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('uploads/', views.uploads, name='uploads'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('national-initiatives/edit/', views.edit_natpage, name='edit_natpage'),
    # path('sports-&-games/edit/', views.edit_gamepage, name='edit_gamepage'),
    # path('cultural-activities/edit/', views.edit_cultpage, name='edit_cultpage'),
    # path('prof-self-initiatives/edit/', views.edit_profpage, name='edit_profpage'),
    # path('entrepreneurship-&-innovation/edit/', views.edit_entrepage, name='edit_entrepage'),
    # path('leadership-&-management/edit/', views.edit_leadpage, name='edit_leadpage'),
    path('change-password', views.change_password, name='change_password'),
    path('reset-password', password_reset, {'template_name': 'accounts/reset_password.html'}, name='password_reset'),
    path('reset-password/done', password_reset_done,
         {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    path('reset-password/confirm/[?P<uidb64>[0-9A-Za-z]+]-(?P<token>.+)',
         password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('accounts/reset-password/complete/', password_reset_complete,
         {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
]
