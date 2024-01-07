from django.urls import path, include
from .views import RegisterAPIView, ProfileViewSet




urlpatterns = [
      path('register/', RegisterAPIView.as_view()),  # for register users
      path('users/', ProfileViewSet.as_view({'get': 'list'})),  # retrieve all users info
      path('user/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'}))  # retrieve concrete user info
]