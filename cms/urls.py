from . import views
from django.urls import path
urlpatterns = [
    path('', views.IndexView, name="index"),
    path('services/', views.ServiceView, name="services"),
    path('systems/', views.SystemView, name="systems"),
    path('contact/', views.ContactView, name="contact"),
    path('resetpassword/', views.resetpassword, name="reset"),
    path('accounts/', views.accounts, name="accounts")
]