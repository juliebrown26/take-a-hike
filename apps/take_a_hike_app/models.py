from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        try: 
            doesExist = User.objects.get(email=postData['email'])
            print("doesExist has passed")
            if doesExist:
                errors['exists'] = "Email already exists. Please sign in."           
        except: 
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First Name should be at least 2 characters"
            if len(postData['first_name']) == 0:
                errors['first_name'] = "Enter a first name."
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last Name should be at least 2 characters"
            if len(postData['last_name']) == 0:
                errors['last_name'] = "Enter a last name."
            if len(postData['password']) < 8:
                errors['password'] = "Password must be at least 8 characters"
            if len(postData['email']) == 0:
                errors['email'] = "Enter an email address."
            if len(postData['password']) == 0:
                errors['password'] = "Enter a password."
            if len(postData['confirm_pw']) == 0:
                errors['confirm_password'] = "Please confirm password"
            if (postData['password']) != (postData['confirm_pw']):
                errors['confirm_pw'] = "Passwords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"User: {self.first_name}, {self.last_name}, {self.email}, {self.password}"

class Trip(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    length = models.IntegerField()
    users = models.ManyToManyField(User, related_name="trips")
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bucket_list(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="bucket_list")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)