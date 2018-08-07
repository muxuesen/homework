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
class CoursecourseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['name']

    def get_name(self,row):
        course_list = row.course_set.all()
        return [{'name': item.name} for item in course_list]

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseLevelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    recommend_courses = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['id','name','level_name','hours','course_slogan','recommend_courses']

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': item.id, 'name': item.name} for item in recommend_list]

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuquestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='OftenAskedQuestion.question')
    answer = serializers.CharField(source='OftenAskedQuestion.answer')
    class Meta:
        model = models.Course
        fields = ['question', 'answer']


 # g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutlineSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['title','content']

    def get_title(self,row):
        coursese_list = row.coursedetail.courseoutline_set.all()
        return [{ 'title': item.title,'content':item.content} for item in coursese_list]


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapterSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['name']

    def get_name(self,row):
        coursese_list = row.coursechapter_set.all()

        return [{ 'name': item.name} for item in coursese_list]

