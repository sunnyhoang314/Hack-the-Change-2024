from django.db import models

class AskForHelp(models.Model):
    user_name = models.CharField(max_length=255)
    people_needed = models.IntegerField()
    task_description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    task_picture = models.ImageField(upload_to='task_pictures/', null=True, blank=True)
    latitude = models.FloatField()  # Latitude of the user asking for help
    longitude = models.FloatField()  # Longitude of the user asking for help
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} needs help with {self.task_description}"
