from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from django.contrib.auth import get_user_model

from .serializers import *

# Create your views here.


class TeacherViewSet(viewsets.ModelViewSet):
    """
    TeacherModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})


class StudentViewSet(viewsets.ModelViewSet):
    """
    StudentModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ProjectModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # student = get_object_or_404(Student, user=request.user)
        # project = student.project
        # queryset = self.queryset.filter(id=project.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.calculate_progression()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ImportantDateViewSet(viewsets.ModelViewSet):
    """
    ImportantDateModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = ImportantDateSerializer
    queryset = ImportantDate.objects.all()

    def list(self, request, *args, **kwargs):
        user = get_user_model().objects.get(request.user)
        if user.groups == [2]:
            student = Student.objects.get(user=user.id)
            queryset = self.queryset.filter(project=student.project)
        elif user.groups == [3]:
            queryset = self.queryset.filter(teacher=user.id)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})


class RequirementViewSet(viewsets.ModelViewSet):
    """
    RequiremenetModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        if not request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            try:
                suggestion = int(request.query_params.get("suggestion"))
                queryset = self.queryset.filter(suggestion=suggestion)
            except:
                return Response(
                    status=404, data={"details": "incorrect query parameters"}
                )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})


class SuggestionViewSet(viewsets.ModelViewSet):
    """
    SuggestionModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        student = get_object_or_404(Student, user=request.user)
        project = student.project
        queryset = self.queryset.filter(project=project.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"datum": serializer.data})
