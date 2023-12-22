from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "schoolstoreapp"  # Corrected app name
urlpatterns = [
    path('', views.home, name='home'),
]