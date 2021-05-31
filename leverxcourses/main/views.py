from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny
from rest_framework.response import Response


from . import serializers, permissions
from .models import Course, Lecture, LectureTask, TaskControl, TaskComments
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)
User = get_user_model()


#################################COURSES#################################
class CourseList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current courses
    and create new courses
    """
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny, DjangoModelPermissions]


    def get_queryset(self):
        logger.info('Getting the list of courses')
        try:
            result = Course.objects.filter(users__id=self.request.user.id)
        except:
            logger.error('Getting the list of courses', CourseList.get_view_name())
        return result

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info('Create course')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_course = serializer.save()
        new_course.users.add(self.request.user)
        headers = self.get_success_headers(serializer.data)
        try:
            result = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            logger.error('Create course error')
        return result


class CourseDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    API endpoint that allows get, update, delete courses
    """
    logger.info('Getting the course ')
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny, DjangoModelPermissions]

    def get_queryset(self):
        try:
           result = Course.objects.filter(users__id=self.request.user.id)
        except:
            logger.error('Getting course detail error', CourseList.get_view_name())
        return result

    def get(self, request, *args, **kwargs):
        try:
            result =  self.retrieve(request, *args, **kwargs)
        except:
            logger.error('Getting course detail error', CourseList.get_view_name())
        return result

    def put(self, request, *args, **kwargs):
        try:
            result = self.update(request, *args, **kwargs)
        except:
            logger.error('Creating course error', CourseList.get_view_name())
        return result


    def delete(self, request, *args, **kwargs):
        try:
            result = self.destroy(request, *args, **kwargs)
        except:
            logger.error('Deletion course detail error', CourseList.get_view_name())
        return result


#################################LECTURES#################################
class LectureList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current lectures
    and create new lectures
    """
    logger.info('Getting the list of lectures')
    serializer_class = serializers.LectureSerializer
    permission_classes = [AllowAny, DjangoModelPermissions]

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
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
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
    logger.info('Getting the list of tasks')
    serializer_class = serializers.TaskSerializer
    permission_classes = [AllowAny, DjangoModelPermissions]

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
    permission_classes = [AllowAny, DjangoModelPermissions]

    def get_queryset(self):
        return LectureTask.objects.filter(lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


##############################TaskControl#################################
class TaskControlList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    API endpoint that allows get list of user's current home tasks
    and create new home tasks
    """
    logger.info('Getting the list of home works')
    serializer_class = serializers.TaskControlSerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return TaskControl.objects.filter(task__lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskControlDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    API endpoint that allows get, update, delete home tasks
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return TaskControl.objects.filter(task__lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##############################TaskComments#################################
class TaskCommentsList(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    """
    API endpoint that allows get list of user's comments in home tasks
    and create new comments
    """
    logger.info('Getting the list of comments')
    serializer_class = serializers.TaskControlSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return TaskComments.objects.filter(taskcontrol__task__lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskCommentsDetail(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    API endpoint that allows get, update, delete comments in home tasks
    """
    serializer_class = serializers.TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return TaskComments.objects.filter(task__lecture__course__users__id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
