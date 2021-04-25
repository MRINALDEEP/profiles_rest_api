#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview=['uses https methods as functions (get,post,update,patch,delete)'
                    'Is Similar to Tradition Django View',
                    'gives you the most control over your application logic',
                    'Is mapped manually to URLS']
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """creates a new hello message with our namne"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        """Handle updates objects"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """Partially updates objects"""
        return Response({'methos':'PATCH'})
    def delete(self,request,pk=None):
        """Deletes Objects"""
        return Response({'method':'DELETE'})