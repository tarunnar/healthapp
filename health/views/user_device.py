import json
import random
from json import JSONDecodeError
import traceback
import math

from django.utils import timezone
from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework import status as reststatus
from rest_framework.response import Response
from django.conf import settings
from health.models import Device, User,UserDevice


class UserDeviceView(APIView):
    def post(self, request, *args, **kwargs):
        response = dict()
        request_data = request.data
        phone = request_data.get("phone")
        imei = request_data.get("imei")
        bought_at = request_data.get("bought_at")
        user_qs =User.objects.filter(phone=phone)
        if not user_qs:
            response["status"], response["message"] = (1, "User not found")
            return Response(response, status=reststatus.HTTP_404_NOT_FOUND)
        user_id = user_qs.first().id
        device_qs = Device.objects.filter(imei=imei)
        if not device_qs:
            response["status"], response["message"] = (1, "Device  not found")
            return Response(response, status=reststatus.HTTP_404_NOT_FOUND)

        device_id = device_qs.first().id
        current_time = timezone.now()
        UserDevice.objects.create(user_id=user_id, device_id=device_id, bought_at=bought_at,
                                  created_at = current_time,
                                  updated_at = current_time )
        response["status"], response["message"] = (0, "Device registered with user")
        return Response(response, status=reststatus.HTTP_200_OK)