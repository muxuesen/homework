from django.http import JsonResponse
from api import models
from rest_framework import serializers
class Abc(serializers.ModelSerializer):
    class Meat:
        model = models.Course
        fields = '__all__'
        depth = 1

class Bcd(serializers.ModelSerializer):
    class Meat:
        model = models.CourseDetail
        fields = '__all__'
        depth = 1