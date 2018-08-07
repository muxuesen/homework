from django.shortcuts import render
from api import models
# Create your views here.
def orms(request):
# a.查看所有学位课并打印学位课名称以及授课老师
    DegreeCourse_list = models.DegreeCourse.objects.all()
    for i in DegreeCourse_list:
        print(i.name,i.teachers.all())

# b.查看所有学位课并打印学位课名称以及学位课的奖学金
        print(i.total_scholarship)

# c.展示所有的专题课
    Course_list = models.Course.objects.filter(degree_course__isnull=True)
    print(Course_list)


# d.查看id = 1的学位课对应的所有模块名称
    obj = models.DegreeCourse.objects.filter(id=1).first()
    print(obj.name)


# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    obj = models.Course.objects.filter(degree_course__isnull=True,id = 1).first()


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
#     obj.


# g.获取id = 1的专题课，并打印该课程相关的课程大纲



# h.获取id = 1的专题课，并打印该课程相关的所有章节



# i.获取id = 1的专题课，并打印该课程相关的所有课时



# 获取id=1的专题课，并打印该课程相关的所有的价格策略