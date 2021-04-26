#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import models
from profiles_api import permissions
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
class HelloViewSets(viewsets.ViewSet):
    """Test API ViewSets"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Returns a hello message"""
        a_viewset=[
            'uses actions- list,create,retrieve,update,partial_update,destroy',
            'Automatically maps URLS using routers',
            'Provides more functinality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    def create(self,request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'method':'GET'})
    def update(self,request,pk=None):
        """Handle Updating a object"""
        return Response({'method':'PUT'})
    def partial_update(self,request,pk=None):
        """Handle partially updating an object"""
        return Response({'method':'PATCH'})
    def destroy(self,request,pk=None):
        """Handle deleteing an object"""
        return Response({'method':'DELETE'})
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class =  serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
class UserLoginAPIView(ObtainAuthToken):
    """Handle user login and generates auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

