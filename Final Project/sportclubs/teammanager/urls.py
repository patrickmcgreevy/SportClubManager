from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.AllClubs.as_view(), name='clubshome'),
    path('myclubs/', views.UserClubs.as_view(), name='userclubs'),
    path('<int:pk>/', views.ClubDetails.as_view(), name='clubdetails'),
    path('<int:pk>/officer_details/', views.ClubOfficerDetails.as_view(), name='clubofficerdetails'),
    path('<int:pk>/change_members/', views.ClubMemberChange.as_view(), name='changemembers'),
]