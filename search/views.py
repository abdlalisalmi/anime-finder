from django.shortcuts import render
from django.conf import settings
from .serializers import UploadImageSerializer

import requests
from decouple import config
import json

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

    def __init__(self):
        data = {}


    def post(self, request):

        API_KEY = config("API_KEY", default="")
        API_URL = f"https://saucenao.com/search.php?api_key={API_KEY}&output_type=2"

        with request.FILES.get("image").open("rb") as image_file:
            files = {'file': image_file}
            response = requests.post(API_URL, files=files)

        self.handle_image_result_response(response)

        return Response(self.data, status=200)


    def handle_image_result_response(self, response):
        response = json.loads(response.text)
        self.data = {
            "anime_name"        : response.get("results")[0].get("data").get("source"),
            "anime_thumbnail"   : response.get("results")[0].get("header").get("thumbnail"),
            "part"              : response.get("results")[0].get("data").get("part"),
            "year"              : response.get("results")[0].get("data").get("year"),
            "source"            : response.get("results")[0].get("data").get("ext_urls")[0],
        }