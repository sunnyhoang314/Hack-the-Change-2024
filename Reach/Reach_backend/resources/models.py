from django.db import models
from django.contrib.auth.models import User

class AskForHelp(models.Model):
    user_name = models.CharField(max_length=255)
    people_needed = models.IntegerField()
    task_description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    task_picture = models.ImageField(upload_to='task_pictures/', null=True, blank=True)
    latitude = models.FloatField()  # Latitude of the user asking for help
    longitude = models.FloatField()  # Longitude of the user asking for help
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='open')

    def __str__(self):
        return f"{self.user_name} needs help with {self.task_description}"

# Model to store user information and points earned
class User(models.Model):
    user_name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)  # Total points earned
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

    # Calculate rank based on points (you can adjust this logic as needed)
    def get_rank(self):
        if self.points < 50:
            return "Novice Helper"
        elif self.points < 150:
            return "Intermediate Helper"
        elif self.points < 300:
            return "Advanced Helper"
        else:
            return "Savior Helper"

# Model for the global leaderboard (this can aggregate points and ranks for each country/city)
class GlobalLeaderboard(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)  # Optional, could be for specific cities
    total_points = models.IntegerField(default=0)
    average_rank = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country} - {self.city if self.city else 'Global'}"