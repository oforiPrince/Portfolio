from django.urls import path

from . import views


urlpatterns = [
    path('',views.DashboardView.as_view(),name='dashboard'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]
