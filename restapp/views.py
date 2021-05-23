from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeList(APIView):

    def get(self,request):
        employee1 = Employee.objects.all()
        serializer = EmployeeSerializer(employee1, many=True)
        return Response(serializer.data)


    def __pos__(self):
        pass