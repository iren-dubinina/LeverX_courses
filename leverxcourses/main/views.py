from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, mixins, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from . import serializers
from .models import Course, Lecture, LectureTask

User = get_user_model()


# Group.objects.create(name='student')
# Group.objects.create(name='lecturer')

#################################COURSES#################################

class CourseList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current courses
    and create new courses
    """
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_course = serializer.save()
        new_course.users.add(self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    API endpoint that allows get, update, delete courses
    """
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#################################LECTURES#################################
class LectureList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current lectures
    and create new lectures
    """
    serializer_class = serializers.LectureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lecture.objects.filter(course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LectureDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = serializers.LectureSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return Lecture.objects.filter(course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#################################TASKS#################################

class TaskList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current tasks
    and create new tasks
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LectureTask.objects.filter(lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    API endpoint that allows get, update, delete tasks
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LectureTask.objects.filter(lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class LecturesViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows lectures to be viewed or edited.
#     """
#     queryset = Lecture.objects.all()
#     serializer_class = LectureSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = (MultiPartParser,)
#
#
# class TaskView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows tasks to be viewed or edited.
#     """
#     queryset = LectureTask.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class TaskControlView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows tasks to be viewed or edited.
#     """
#     queryset = TaskControl.objects.all()
#     serializer_class = TaskControlSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class TaskCommentView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows tasks to be viewed or edited.
#     """
#     queryset = TaskComments.objects.all()
#     serializer_class = TaskCommentSerializer
#     permission_classes = [permissions.IsAuthenticated]
