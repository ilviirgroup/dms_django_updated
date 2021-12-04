from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Messages', MsgCreate)
router.register(r'Files', FileCreate)
router.register(r'Users', SenCreate)
router.register(r'Departments', RecCreate)


urlpatterns = [
    path('', include(router.urls)),    
]