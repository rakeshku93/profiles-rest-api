from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView """

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiView = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Is manually mapped to the URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiView': an_apiView})

    # def post(self,)
