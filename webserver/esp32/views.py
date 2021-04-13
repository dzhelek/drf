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


class MotorSettingView(viewsets.ModelViewSet):
    queryset = models.MotorSetting.objects.all()
    serializer_class = serializers.MotorSettingSerializer


class TimingSettingView(viewsets.ModelViewSet):
    queryset = models.TimingSetting.objects.all()
    serializer_class = serializers.TimingSettingSerializer
