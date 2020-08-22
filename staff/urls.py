from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('student-details/<int:id>/', views.uploads, name='uploads'),
    path('search/', views.search, name='search'),
    # path('search-results-ajax/', views.search_results_ajax, name='search_results_ajax'),
    path('national-initiatives/view/<int:uid>/<int:id>/', views.view_natpage, name='view_natpage'),
    path('sports-&-games/view/<int:uid>/<int:id>/', views.view_gamepage, name='view_gamepage'),
    path('cultural-activities/view/<int:uid>/<int:id>/', views.view_cultpage, name='view_cultpage'),
    path('prof-self-initiatives/view/<int:uid>/<int:id>/', views.view_profpage, name='view_profpage'),
    path('entrepreneurship-&-innovation/view/<int:uid>/<int:id>/', views.view_entrepage, name='view_entrepage'),
    path('leadership-&-management/view/<int:uid>/<int:id>/', views.view_leadpage, name='view_leadpage'),
    path('national-initiatives/approve/<int:uid>/<int:id>/', views.approve_natpage, name='approve_natpage'),
    path('sports-&-games/approve/<int:uid>/<int:id>/', views.approve_gamepage, name='approve_gamepage'),
    path('cultural-activities/approve/<int:uid>/<int:id>/', views.approve_cultpage, name='approve_cultpage'),
    path('prof-self-initiatives/approve/<int:uid>/<int:id>/', views.approve_profpage, name='approve_profpage'),
    path('entrepreneurship-&-innovation/approve/<int:uid>/<int:id>/', views.approve_entrepage, name='approve_entrepage'),
    path('leadership-&-management/approve/<int:uid>/<int:id>/', views.approve_leadpage, name='approve_leadpage')
]
