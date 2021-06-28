from django.db import models
from django.contrib.auth.models import User

# auto_now=False, auto_now_add=False, null=True, blank=True
class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_work = models.TextField(max_length=100)
    start_break = models.TextField(max_length=100, null=True, blank=True)
    end_break = models.TextField(max_length=100, null=True, blank=True)
    end_work = models.TextField(max_length=100, null=True, blank=True)
    away = models.SmallIntegerField(default=0)
    actual_worked_hours = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    # datetime.datetime.strptime(datetime.datetime.today().strftime('%m/%d/%Y, %H:%M:%S'), '%m/%d/%Y, %H:%M:%S')

    def __str__(self):
        return f"{self.user}|{self.start_work}|{self.start_break}|{self.end_break}|{self.end_work}|{self.away}"


class Break(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_break = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_break = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def str(self):
        return f"{self.user}|{self.start_break}|{self.end_break}"

