from django.views import View
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication, permissions


class HomeView(View):
    
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)



class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

class SearchView(APIView):
    """
    docstring
    """
    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]
    

    def post(self, request):
        return Response({"ddd": "sss"}, status=200)