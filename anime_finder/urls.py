from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    
    path('search/', include("search.urls")),
]
