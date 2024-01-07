from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Player
from .serializers import UserSerializer, RegisterSerializer, PlayerSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class ProfileViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response({'players': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Player.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(user)
        return Response(serializer.data)

