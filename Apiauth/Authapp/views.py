from django.shortcuts import render
from django.http import request, JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import UserLoginSerializer
from .models import Login

# Create your views here.

def Home(request):
    return render(request,'index.html' )


def Loginuser(request):
     if request.method == "GET":
        account = Login.objects.all()
        serializer = UserLoginSerializer(account, many=True)
        return JsonResponse(serializer.data, safe=False)

     elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)


