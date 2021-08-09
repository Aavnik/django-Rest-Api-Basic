from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import Todoserialize
from .models import *
from rest_framework.views import APIView

# Create your views here.
@api_view()
def home(request): # All Todo
    todo_obj = Todomodel.objects.all()
    serilize_obj = Todoserialize(todo_obj, many = True)
    
    return Response({'status':200,"message": "all ok", 'Data':serilize_obj.data})

# Add Todo
@api_view(['POST'])
def addtodo(request):
    data = request.data
    serializer_obj = Todoserialize(data=data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response({'status':200,'Message': "Todo Saved"})
    return Response({'status':400, 'error':"Todo Not Saved"})

# Update Todo
@api_view(['PATCH'])
def updatetodo(request):
    data = request.data
    todo_obj = Todomodel.objects.get(id =data.get('id'))
    serializer_obj = Todoserialize(todo_obj,data=data, partial = True)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response({'status':200,'Message': "Todo Updated"})
    return Response({'status':400, 'error':"Id is not vaild"})

# Delete Todo
@api_view(['DELETE'])
def deletetodo(request):
    data = request.data
    try:
        todo_obj = Todomodel.objects.get(id =data.get('id'))
        todo_obj.delete()
        return Response({'status':200,'Message': "Todo Deleted"})
    except Exception as e:
        print(e)    
    
    return Response({'status':400, 'error':"Id is not vaild"})
    

# Class view API    
class Todoview(APIView): # All Todo
    def get(self, request):
        todo_obj = Todomodel.objects.all()
        serilize_obj = Todoserialize(todo_obj, many = True)
    
        return Response({'status':200,"message": "all ok", 'Data':serilize_obj.data})

    # Add Todo   
    def post(self, request):
        data = request.data
        serializer_obj = Todoserialize(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({'status':200,'Message': "Todo Saved"})
        return Response({'status':400, 'error':"Todo Not Saved"})

    #Update Todo    
    def patch(self, request):
        data = request.data
        todo_obj = Todomodel.objects.get(id =data.get('id'))
        serializer_obj = Todoserialize(todo_obj,data=data, partial = True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({'status':200,'Message': "Todo Updated"})
        return Response({'status':400, 'error':"Id is not vaild"})

    # Delete Todo    
    def delete(self, request):
        data = request.data
        try:
            todo_obj = Todomodel.objects.get(id =data.get('id'))
            todo_obj.delete()
            return Response({'status':200,'Message': "Todo Deleted"})
        except Exception as e:
            print(e)    
    
        return Response({'status':400, 'error':"Id is not vaild"})