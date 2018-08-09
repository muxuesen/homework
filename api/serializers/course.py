from rest_framework import serializers
from api import models
class CourseDetailSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    recommend_courses = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id','name','level_name', 'hours', 'course_slogan', 'recommend_courses']

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': item.id, 'name': item.name} for item in recommend_list]

#c. 展示所有的专题课
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','name']

# d. 查看id=1的学位课对应的所有模块名称
class CoursecourseSerializer(serializers.Serializer):
    course = serializers.SerializerMethodField()

    def get_course(self,row):
        return [item.name for item in row.course_set.all()]

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseLevelSerializer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.SerializerMethodField()

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [item.name for item in recommend_list]

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuquestionSerializer(serializers.Serializer):
    asked_question = serializers.SerializerMethodField()

    def get_asked_question(self, row):
        return [item.question for item in row.asked_question.all()]


 # g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutlineSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()

    def get_title(self,row):

        return [item.title for item in row.coursedetail.courseoutline_set.all()]


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapterSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()

    def get_name(self,row):

        return [item.name for item in row.coursechapters.all()]

