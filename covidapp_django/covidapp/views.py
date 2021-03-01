# from django.shortcuts import render
from rest_framework import generics
from .serializers import StateSerializer, LocationSerializer, FeedbackSerializer
from .models import State, Location, Feedback

# Create your views here.
class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

# Create views for Locations
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Create views for Comments
class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer