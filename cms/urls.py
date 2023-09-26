from . import views
from django.urls import path
urlpatterns = [
    path('', views.indexfr, name="testhome"),
    path('resetpassword/', views.resetpassword, name="reset")
]