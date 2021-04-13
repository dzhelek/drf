from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('notification', views.NotificationView)
router.register('settings/motor', views.MotorSettingView)
router.register('settings/timing', views.TimingSettingView)

urlpatterns = [
    path('', include(router.urls)),
    path('sensors', views.SensorsValueView.as_view(), {"pk": 1}),
]
