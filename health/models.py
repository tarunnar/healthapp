from django.db import models

# Create your models here.
class User(models.Model):
    client = 1
    admin = 2
    role_choices = ((client, "client"),
                    (client, "admin"))
    name = models.CharField(max_length=14)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    email_id = models.EmailField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=role_choices, default=role_choices[0][0])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        unique_together = [['phone']]
        db_table = "users"


class Device(models.Model):
    height = 1
    weight = 2
    heart_rate = 3
    calorie = 4
    device_choices = ((height, "height"),
                      (weight, "weight"),
                      (heart_rate, "heart_rate"),
                      (calorie, "calorie"),
                      )
    imei = models.CharField(max_length=20)
    device_type = models.PositiveSmallIntegerField(choices=device_choices, default=device_choices[0][0])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        unique_together = [['imei']]
        db_table = "devices"


class UserDevice(models.Model):

    user_id = models.IntegerField()
    device_id = models.IntegerField()
    bought_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        unique_together = [['user_id', 'device_id']]
        db_table = "user_devices"


class Attributes(models.Model):
    height = 1
    weight = 2
    heart_rate = 3
    calorie = 4
    attribute_choices = ((height, "height"),
                      (weight, "weight"),
                      (heart_rate, "heart_rate"),
                      (calorie, "calorie"),
                      )
    user_id = models.IntegerField()
    device_id = models.IntegerField()
    attribute_id = models.PositiveSmallIntegerField(choices=attribute_choices)
    value = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "attribute_values"

