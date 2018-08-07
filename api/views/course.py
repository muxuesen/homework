from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api import models
from django import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import CourseSerializer, CourseDetailSerializer, CoursecourseSerializer, \
    CourseChapterSerializer, CourseQuquestionSerializer, CourseOutlineSerializer, CourseLevelSerializer

from api.utils.response import BaseResponse
# Create your views here.
class CoursesView(APIView):
    """
    课程视图
    """
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            #从数据库取数据
            queryset = models.Course.objects.all()
            #分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            #分页结果序列化
            ser = CourseSerializer(course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

class CourseDetailView(APIView):

    def get(self,request,pk,*args,**kwargs):
        ret = BaseResponse()
        try:
            course = models.Course.objects.filter(id=pk)
            #序列化
            ser = CourseDetailSerializer(instance=course)
            ret.data = ser.data
            print(ret.data)
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"

        return Response(ret.dict)


#c. 展示所有的专题课
class CourseView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            #从数据库取数据
            queryset = models.Course.objects.all()
            ser = CourseSerializer(queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)


# d. 查看id=1的学位课对应的所有模块名称
class CoursecourseView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            #从数据库取数据
            course_list = models.DegreeCourse.objects.get(id=1)
            ser = CoursecourseSerializer(course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseLevelView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库取数据
            course_list = models.DegreeCourse.objects.get(id=1)
            ser = CourseLevelSerializer(course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuquestionView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            course_list = models.Course.objects.get(id=1)
            ser = CourseQuquestionSerializer(course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)


 # g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutlineView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            course_list = models.Course.objects.get(id=1)
            ser = CourseOutlineSerializer(course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapterView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库取数据
            chapter_list = models.Course.objects.get(id=1)
            ser = CourseChapterSerializer(chapter_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)






