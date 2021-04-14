from django.utils import timezone
from rest_framework import generics, viewsets

from . import models, serializers


class SensorsValueView(generics.RetrieveUpdateAPIView):
    queryset = models.SensorsValue.objects.all()
    if not models.SensorsValue.objects.count():
        models.SensorsValue.objects.create()
    serializer_class = serializers.SensorsValueSerializer


class NotificationView(generics.RetrieveUpdateAPIView):
    queryset = models.Notification.objects.all()
    if not models.Notification.objects.count():
        models.Notification.objects.create()
    serializer_class = serializers.NotificationSerializer

    def retrieve(self, *args, **kwargs):
        motor_settings = models.MotorSetting.objects.all()
        notifications = models.Notification.objects.first()
        if any(ms.time_on < timezone.localtime().time() < ms.time_off for ms in motor_settings):
            notifications.is_motor_on = True
            notifications.save()
        else:
            if notifications.is_motor_on:
                notifications.is_motor_on = False
                notifications.save()
        return super().retrieve(*args, **kwargs)


class MotorSettingView(viewsets.ModelViewSet):
    queryset = models.MotorSetting.objects.all()
    serializer_class = serializers.MotorSettingSerializer


class TimingSettingView(viewsets.ModelViewSet):
    queryset = models.TimingSetting.objects.all()
    serializer_class = serializers.TimingSettingSerializer
