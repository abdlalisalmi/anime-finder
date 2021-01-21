from django.shortcuts import render
from .serializers import UploadImageSerializer

import requests
from decouple import config

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication, permissions



class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

class SearchView(APIView):
    """
    This class is for handle the search functionality.
    """
    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    API_KEY = config("API_KEY", default="")
    URL = f"https://saucenao.com/search.php?api_key={API_KEY}&output_type=2"

    def post(self, request):
        serializer = UploadImageSerializer(request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
        # files = {'upload_file': request.FILES.get("image")}
        # r = requests.post(self.URL, files=files)
        return Response({"r":"r"}, status=200)