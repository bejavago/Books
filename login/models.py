from django.db import models

class User1(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book1(models.Model):
    title = models.CharField(default="Title*", max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(default="Description*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Book ID: ({self.id})| Title: {self.title}| Network: {self.network}| Release Date: {self.release_date}| Description: {self.description} ||"