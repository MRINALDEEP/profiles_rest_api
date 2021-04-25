#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview=['uses https methods as functions (get,post,update,patch,delete)'
                    'Is Similar to Tradition Django View',
                    'gives you the most control over your application logic',
                    'Is mapped manually to URLS']
        return Response({'message':'Hello','an_apiview':an_apiview})

