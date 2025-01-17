from django.db import models

# Here we will have the real user profile, so we can add more fields to the user

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#daqui pra baixo foi add por pablo depois
"""
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

"""
