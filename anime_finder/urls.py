from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),

    path('search/', include("search.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
