from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name='home' ),
    path('notes/', views.get_data , name='get_data' ),
    path('logout/', views.logout_view , name='logout_view' ),
    path('login/', views.login_view , name='login_view' ),
]
