from django.db import models


class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    joined_date = models.DateField(null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

