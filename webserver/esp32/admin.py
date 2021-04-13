from django.contrib import admin

from . import models


@admin.register(models.SensorsValue)
class SensorsValueAdmin(admin.ModelAdmin):
    list_display = 'water_level', 'temperature'

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = 'has_not_food', 'has_not_water', 'is_heater_on', 'is_motor_on'

@admin.register(models.TimingSetting)
class TimingSettingAdmin(admin.ModelAdmin):
    list_display = 'last_filled', 'finishing_time'

@admin.register(models.MotorSetting)
class MotorSettingAdmin(admin.ModelAdmin):
    list_display = 'time_on', 'time_off'
