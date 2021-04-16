from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMINISTRATOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMINISTRATOR, 'Administrator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

     # returns the url to 'profile_detail.html' 
    def get_absolute_url(self):
        return reverse("profile_detail")  

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        print('new user and profile added')


    Profile.objects.get_or_create(user=instance)
    instance.profile.save()

