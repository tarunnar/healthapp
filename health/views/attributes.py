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
from health.models import Device, User,UserDevice, Attributes


class AttributesView(APIView):
    def post(self, request, *args, **kwargs):
        response = dict()
        request_data = request.data
        phone = request_data.get("phone")
        imei = request_data.get("imei")
        value = request_data.get("value")
        user_qs =User.objects.filter(phone=phone)
        user_id = user_qs.first().id
        device_qs = Device.objects.filter(imei=imei)
        device_obj = device_qs.first()
        device_id = device_obj.id
        attribute_type = device_obj.device_type
        current_time = timezone.now()
        Attributes.objects.create(user_id=user_id, device_id=device_id, value=value,
                                  attribute_id =attribute_type,
                                  created_at = current_time,
                                  updated_at = current_time )
        response["status"], response["message"] = (0, "Stat registered successfully")
        return Response(response, status=reststatus.HTTP_200_OK)