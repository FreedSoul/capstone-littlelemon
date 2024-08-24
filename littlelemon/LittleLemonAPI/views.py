from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, authentication_classes

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    
@api_view()    
@permission_classes([IsAuthenticated])
# @authentication_classes([])
def msg(request):
    return Response({"message":"This view is protected"})