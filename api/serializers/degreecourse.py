from rest_framework import serializers
from api import models

# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ["name", 'teacher_name']

    def get_teacher_name(self, row):
        teacher_list = row.teachers.all()

        return [{'name': item.name} for item in teacher_list]

 # b.查看所有学位课并打印学位课名称以及学位课的奖学金
class ScholarshipsSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ["name","value",]

    def get_value(self, row):
        scholarship_list = row.scholarship_set.all()

        return [{'name': item.value} for item in scholarship_list]


