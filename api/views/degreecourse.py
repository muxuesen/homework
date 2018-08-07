from api.serializers.degreecourse import DegreeCourseSerializer, ScholarshipsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from api.utils.response import BaseResponse
from api import models


# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()
            # 序列化
            ser = DegreeCourseSerializer(degree_list,many=True)
            ret.data = ser.data

        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

 # b.查看所有学位课并打印学位课名称以及学位课的奖学金
class ScholarshipsView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()

            ser = ScholarshipsSerializer(degree_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"

        return Response(ret.dict)
