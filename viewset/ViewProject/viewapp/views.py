from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class TestViewSet(viewsets.ViewSet):

    def list(self,request):
        stud = Student.objects.all()
        serializer =StudentSerializer(stud, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer =StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created'})
        else:
            return Response(serializer.errors)

    def retrieve(self,request,pk):
        try:
             stud = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer =StudentSerializer(stud)
        return Response(serializer.data)

    def update(self,request,pk):
        stud = Student.objects.get(pk=pk)
        serializer =StudentSerializer(stud, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Updated'})
        else:
            return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        stud = Student.objects.get(pk=id)
        stud.delete()
        return Response({'msg':'Deleted'})




