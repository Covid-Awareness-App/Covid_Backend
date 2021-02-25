from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100, blank=True, default="State Name")
    img_icon = models.TextField()
    average_daily_cases = models.IntegerField(default=1000)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.ForeignKey(State, on_delete=models.CASCADE, related_name='locations', null=True)
    business_name = models.CharField(max_length=100, blank=True, default="Business Name")
    business_img = models.TextField()
    address = models.TextField()
    hours = models.CharField(max_length=100, blank=True, default="Business Hours")
    contact_number = models.CharField(max_length=100, blank=True, default="Business Contact Information")
    offers = models.TextField()

    def __str__(self):
        return self.business_name
