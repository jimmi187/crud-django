from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all-emp' : 'api/employee',
        'add-emp' : 'api/employee/create',
        'get-by-id' : 'api/employee/<pk>',
        'update-emp' : 'api/employee/<pk>/update',
        'delete-emp' : 'api/employee/<pk>/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_employee(request):
    empoloyee = EmployeeSerializer(data = request.data)
    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError('this data allready exist')
    
    if empoloyee.is_valid():
        empoloyee.save()
        return Response(empoloyee.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    
@api_view(['GET'])
def view_employees(request):

    if request.query_params:
        employees = Employee.objects.filter(**request.query_param.dic())
    else:
        employees = Employee.objects.all()
    
    if employees:
        datas = EmployeeSerializer(employees, many=True)
        return Response(datas.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_employee_by_id(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return Response(EmployeeSerializer(employee).data)
   



@api_view(['PUT'])
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    data = EmployeeSerializer(instance=employee, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_employee_by_id(reqest, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
