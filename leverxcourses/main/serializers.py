from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

User = get_user_model()

from .models import Course, Lecture, LectureTask, TaskControl, TaskComments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    date = serializers.DateField()
    users = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=User.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'date', 'users']

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.users.set(validated_data.get('users', instance.users))
        instance.save()
        return instance


class LectureSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    theme = serializers.CharField(required=False)
    slides = serializers.FileField(required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Lecture
        fields = ['theme', 'slides', 'id']

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.theme = validated_data.get('theme', instance.theme)
        instance.slides = validated_data.get('slides', instance.slides)
        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    text = serializers.CharField()
    lecture = serializers.PrimaryKeyRelatedField(queryset=Lecture.objects.all())

    class Meta:
        model = LectureTask
        fields = ['id', 'name', 'text', 'lecture']

    def create(self, validated_data):
        return LectureTask.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class TaskControlSerializer(serializers.Serializer):
    datetime = serializers.DateTimeField('DateTime', required=False)
    attachment = serializers.CharField()
    checked = serializers.BooleanField('Checked', default=False)
    grade = serializers.IntegerField(required=False)
    task = serializers.PrimaryKeyRelatedField(queryset=LectureTask.objects.all())

    class Meta:
        model = TaskControl
        fields = ['datetime', 'attachment', 'checked', 'grade', 'task']

    def create(self, validated_data):
        return TaskControl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        instance.checked = validated_data.get('checked', instance.checked)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance


class TaskCommentsSerializer(serializers.Serializer):
    comment = serializers.CharField()
    datetime = serializers.DateTimeField(required=False)
    taskcontrol = serializers.PrimaryKeyRelatedField(queryset=TaskControl.objects.all())

    class Meta:
        model = TaskComments
        fields = ['comment', 'datetime', 'taskcontrol']

    def create(self, validated_data):
        return TaskComments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance


class CourseUsersSerializer(serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(many=True, required=True, queryset=User.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'users']

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.users += validated_data.get('users')
        instance.save()
        return instance
