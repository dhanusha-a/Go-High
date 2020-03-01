from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self):
        return self.Email
