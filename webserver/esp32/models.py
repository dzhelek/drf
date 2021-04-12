from django.db import models


class SensorsValue(models.Model):
    water_level = models.PositiveSmallIntegerField(default=0)
    temperature = models.SmallIntegerField(default=0)


class Notification(models.Model):
    has_not_water = models.BooleanField(default=False)
    has_not_food = models.BooleanField(default=False)
    is_heater_on = models.BooleanField(default=False)
    is_motor_on = models.BooleanField(default=False)


class MotorSetting(models.Model):
    time_on = models.TimeField()
    time_off = models.TimeField()


class TimingSetting(models.Model):
    last_filled = models.DateTimeField()
    finishing_time = models.FloatField()
