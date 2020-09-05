from django.urls import path, include
from health.views.user import UserView
from health.views.device import DeviceView
from health.views.user_device import UserDeviceView
from health.views.attributes import AttributesView

urlpatterns_versioned = [
    path("register_user/", UserView.as_view(), name="register_user"),
    path("register_device/", DeviceView.as_view(), name="register_device"),
    path("map_user_device/", UserDeviceView.as_view(), name="map_user_device"),
    path("record_attributes/", AttributesView.as_view(), name="record_attributes"),
]