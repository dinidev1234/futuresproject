from django.urls import path, include
from .views import RegisterAPIView, ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet, basename='user')






urlpatterns = [
      path('register/', RegisterAPIView.as_view()),  # for register users
      path('', include(router.urls))  # set of urls 'user' for retrieve all players, user/id for retrieve concrete player info
]
