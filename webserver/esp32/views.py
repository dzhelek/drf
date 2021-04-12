from rest_framework import viewsets

from . import models, serializers


class SensorsValueView(viewsets.ModelViewSet):
    queryset = models.SensorsValue.objects.all()
    serializer_class = serializers.SensorsValueSerializer


class NotificationView(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer


class MotorSettingView(viewsets.ModelViewSet):
    queryset = models.MotorSetting.objects.all()
    serializer_class = serializers.MotorSettingSerializer


class TimingSettingView(viewsets.ModelViewSet):
    queryset = models.TimingSetting.objects.all()
    serializer_class = serializers.TimingSettingSerializer
