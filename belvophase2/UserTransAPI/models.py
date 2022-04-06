from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Transactions(models.Model):
    reference = models.CharField(max_length=255, primary_key=True, unique=True)
    account = models.CharField(max_length=255)
    date = models.DateField(default=None)
    amount = models.FloatField(default=0.0)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
