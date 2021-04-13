from rest_framework import serializers

from . import models


class SensorsValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorsValue
        fields = 'water_level', 'temperature'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = 'has_not_water', 'has_not_food', 'is_heater_on', 'is_motor_on'


class MotorSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MotorSetting
        fields = '__all__'


class TimingSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingSetting
        fields = '__all__'
