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
from health.models import Device


class DeviceView(APIView):
    def post(self, request, *args, **kwargs):
        response = dict()
        request_data = request.data
        imei = request_data.get("imei")
        device_type = request_data.get("device_type")
        current_time = timezone.now()
        device_map = {
            "height": 1,
            "weight": 2,
            "heart_rate": 3,
            "calorie": 4
        }
        device_type = device_map.get(device_type)
        if not device_type:
            response["status"], response["message"] = (1, "Invalid device type")
            return Response(response, status=reststatus.HTTP_400_BAD_REQUEST)

        Device.objects.create(imei=imei, device_type=device_type, created_at= current_time, updated_at=current_time)
        response["status"], response["message"] = (0, "Device created successfully")
        return Response(response, status=reststatus.HTTP_200_OK)

