from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
# from django.http import JsonResponse

from .models import UserProfile

from profiles_api import serializers
from profiles_api import permissions


class HelloApiView(APIView):
    '''Test API Viewssss'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        ''' Handle updating an object '''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        ''' Handle a partial update of an object '''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        ''' Delete an object '''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a hello message'''
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new hello message'''
        serializer = self.serializer_class(data=request.data)
        # print(serializer)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handle getting an object by its ID'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''Handle updating part of an object'''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''Handle removing an object'''
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


"""
class UserProfileApiView(APIView):
    '''my code using APIView'''
    serializer_class = serializers.UserProfileSerializer

    def get(self, request, pk=None):
        '''Handle getting an object by its ID'''
        user = UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(user, many=True)
        return Response(serializer.data)

        # user = UserProfile.objects.all()
        # serializer = serializers.UserProfileSerializer(user, many=True)
        # return JsonResponse(serializer.data, safe=False)

    # def get(self, request, pk):
    #     user = UserProfile.objects.get(id=pk)
    #     serializer = serializers.UserProfileSerializer(user)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     print(serializer)

    #     if serializer.is_valid():
    #         email = serializer.validated_data.get('email')
    #         name = serializer.validated_data.get('name')
    #         password = serializer.validated_data.get('password')
    #         return Response({'email': email, 'name': name, 'password': password})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
"""
