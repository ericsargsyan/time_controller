from django.db import models
from django.contrib.auth.models import User


class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_work = models.DateTimeField()
    start_break = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_break = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_work = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    away = models.IntegerField(default=0)
    # away = end_break - start_break
    actually_worked_hours = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}|{self.start_work}|{self.start_break}|{self.end_break}|{self.end_work}"
