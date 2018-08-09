from django.conf.urls import url
from api.views import course
from api.views import degreecourse
from api.views import shoppingcar

urlpatterns = [
    url(r'^courses/$', course.CoursesView.as_view()),

    url(r'^courses/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),

    # a.查看所有学位课并打印学位课名称以及授课老师
    url(r'^degreecourse/$', degreecourse.DegreeCourseView.as_view()),

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    url(r'^scholarships/$', degreecourse.ScholarshipsView.as_view()),

    # c. 展示所有的专题课
    url(r'^course/$', course.CourseView.as_view()),

    # d. 查看id=1的学位课对应的所有模块名称
    url(r'^coursecourse/$', course.CoursecourseView.as_view()),

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    url(r'^courselevel/$', course.CourseLevelView.as_view()),

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    url(r'^courseququestion/$', course.CourseQuquestionView.as_view()),

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    url(r'^courseoutline/$', course.CourseOutlineView.as_view()),

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    url(r'^coursechapter/$', course.CourseChapterView.as_view()),


    url(r'^shoppingcar/$', shoppingcar.ShoppingCarView.as_view({"post":"create","get":"list","delete":"destroy", "put": "update"})),
    # url(r'^shoppingcar/(?P<pk>\d+)$', shoppingcar.ShoppingCarView.as_view({"post":"create","get":"list"})),

]