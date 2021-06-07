from django.db.models import query
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import UserLoginSerializer
from .models import Login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from django.http import request
from rest_framework.decorators import action
from rest_framework.decorators import api_view


# Create your views here.

def Home(request):
    return render(request,'index.html' )


class LoginUser(viewsets.ModelViewSet):
    queryset=Login.objects.all()
    serializer_class=UserLoginSerializer




class ApiEg(APIView):
    def get(self,request):
        user= Login.objects.all()
        serializer=UserLoginSerializer(user,many=True)
        return Response(serializer.data)
   
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)










