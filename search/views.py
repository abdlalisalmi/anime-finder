from django.shortcuts import render
from django.conf import settings
from .serializers import UploadImageSerializer

import time
import requests
from decouple import config

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from .models import UploadImage


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

class SearchView(APIView):
    """
        This class is for handle the search functionality.
    """
    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    def post(self, request):

        API_KEY = config("API_KEY", default="")
        API_URL = f"https://saucenao.com/search.php?api_key={API_KEY}&output_type=2"

        with request.FILES.get("image").open("rb") as image_file:
            files = {'file': image_file}
            r = requests.post(API_URL, files=files)
        return Response({"r":r}, status=200)
