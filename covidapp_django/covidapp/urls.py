from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('state/', views.StateList.as_view(), name='state_list'),
    path('state/<int:pk>', views.StateDetail.as_view(), name='state_detail'),
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
]