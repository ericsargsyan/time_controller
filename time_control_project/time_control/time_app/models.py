from django.db import models
from django.contrib.auth.models import User


class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_work = models.DateTimeField()
    # start_break = models.DateTimeField()
    # end_work = models.DateTimeField()
    end_work = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    # end_work = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "aaa"
