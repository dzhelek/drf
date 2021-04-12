from rest_framework import serializers

from . import models


class SensorsValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorsValue
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'


class MotorSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MotorSetting
        fields = '__all__'


class TimingSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimingSetting
        fields = '__all__'