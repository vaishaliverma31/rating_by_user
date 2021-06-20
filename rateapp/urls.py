from django.urls import path
from .views import *


urlpatterns =[
    path('appapi',appapiview.as_view()),
    path('appapi',Appapiview.as_view()),
    path('userapi',userdefineview.as_view()),
    path('register',RegisterUser.as_view()),
]