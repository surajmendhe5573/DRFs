from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.http import Http404

class ItemList(APIView):
    """
    List all Items and create new item.
    """
    def get(self, request):
        items= Item.objects.all()
        serializer= ItemSerializer(items, many= True)
        return Response(serializer.data)
    
    def post(relf, request):
        serializer= ItemSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)