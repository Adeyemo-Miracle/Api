from django.shortcuts import render
from rest_framework.decorators import api_view
from app.serializer import appSerializer
from .models import App
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def createtodo(request):
    record = appSerializer(data = request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def alltodo(request):
    record = App.objects.all()
    info = appSerializer(record, many = True)
    return Response(info.data)

@api_view(['DELETE'])
def deletetodo(request, id):
    record = App.objects.get(id = id)
    record.delete()
    return Response('Todo deleted Successfully')

@api_view(['GET'])
def tododetails(request, id):
    record = App.objects.get(id = id)
    info = appSerializer(record, many = False)
    return Response(info.data)

@api_view(['GET'])
def todoedit(request, id):
    record = App.objects.get(id = id)
    info = appSerializer(data = request.data, instance = record)
    if info.is_valid():
        info.save()
        return Response('Updated Successfully')