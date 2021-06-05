from django.db import models


class User_data(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    real_name = models.CharField(blank=True, null=True, max_length=256)
    tz = models.CharField(blank=True, null=True, max_length=256)


class Activity_periods(models.Model):
    user = models.ForeignKey(User_data, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=32)
    end_time = models.CharField(max_length=32)
