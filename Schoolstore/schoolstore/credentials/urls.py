from . import views
from django.urls import path

app_name = 'credentials'
urlpatterns = [

    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('formpage/',views.formpage,name='formpage'),
    # path('logout',views.logout,name='logout')
]