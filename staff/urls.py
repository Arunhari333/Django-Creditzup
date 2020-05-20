from django.urls import path
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)

app_name = 'staff'

urlpatterns = [
    path('home', views.home, name='home'),
    path('student-details/<int:id>', views.uploads, name='uploads'),
    path('search', views.search, name='search')
]