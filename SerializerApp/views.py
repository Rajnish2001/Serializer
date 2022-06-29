from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def student_details(request):
    stu = Student.objects.get(id=1) #Dict value
    serializer = StudentSerializer(stu) #serializer data
    # json_data = JSONRenderer().render(serializer.data) #Render serializer data into json formate
    # return HttpResponse(json_data,content_type='application/json') #send response to the API Application
    return JsonResponse(serializer.data)

def student_data(request):
    stu = Student.objects.all() #None Dict Data
    serializer = StudentSerializer(stu, many=True) #serialized data
    # json_data = JSONRenderer().render(serializer.data) #Render serialized data into json formate
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
