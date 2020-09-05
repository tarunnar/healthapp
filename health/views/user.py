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
from health.models import User


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        response = dict()
        request_data = request.data
        name = request_data.get("name")
        email_id = request_data.get("email_id")
        phone = request_data.get("phone")
        password = request_data.get("password")
        user_qs = User.objects.filter(phone=phone)
        current_time = timezone.now()
        if user_qs:
            response["status"], response["message"] = (1, "User already exists")
            return Response(response, status=reststatus.HTTP_409_CONFLICT)
        try:
            User.objects.create(name=name, email_id=email_id, phone=phone, password=password,
                                created_at=current_time, updated_at=current_time)
            response["status"], response["message"] = (0, "User created successfully")
            return Response(response, status=reststatus.HTTP_200_OK)
        except Exception as e:
            response["status"], response["message"] = (1, "Some error while creating user")
            return Response(response, status=reststatus.HTTP_500_INTERNAL_SERVER_ERROR)
