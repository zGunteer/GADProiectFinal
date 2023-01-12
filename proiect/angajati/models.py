from django.db import models

# Create your models here.

class Angajati(models.Model):

    nume = models.CharField(max_length=100)
    varsta = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.nume} -> {self.varsta}"


class Log(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
