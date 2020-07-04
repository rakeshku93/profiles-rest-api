from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test APIView """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiView = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Is manually mapped to the URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiView': an_apiView})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling by updating the object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of the object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': "DELETE"})
