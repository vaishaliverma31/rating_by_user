from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from  rest_framework.views import  APIView
from rest_framework.response import Response

# Create your views here.
class appapiview(ListCreateAPIView):
    queryset = application.objects.all()
    serializer_class = applicationsserializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
class RegisterUser(APIView) :
    def post(self,request):
        serializer=userseializer(data=request.data)

        if not serializer.is_valid():
               print(serializer.errors)
               return Response ({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh),
        'access': str(refresh.access_token),'message':'your data is saved'})





class Appapiview(RetrieveUpdateDestroyAPIView)  :
    queryset = application.objects.all()
    serializer_class = applicationsserializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class userdefineview(ListCreateAPIView):
    queryset = user_define.objects.all()
    serializer_class = user_defineserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
     app_id=serializer.validated_data.get('app')
     print(app_id)
     serializer.save()
     rating=[]
     j=0
     for i in user_define.objects.filter(app=app_id.id):
         j=j+(i.rating)
         rating.append(i.rating)
     count=len(rating)
     formula=j/count
     app_query=application.objects.get(id=app_id.id)
     app_query.overall_rating=formula
     app_query.save()
     print(formula)
     review_list = {}
     for i in user_define.objects.filter(app=app_id.id):
         review_list[i.user]=[i.review]
     app_querys = application.objects.get(id=app_id.id)
     app_querys.overall_review = review_list
     app_querys.save()