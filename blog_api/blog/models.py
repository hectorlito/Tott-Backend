from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title


class FM(models.Model):
    challenge = models.CharField(max_length=500)
    writeup = models.TextField()

    def __str__(self):
        return self.challenge
