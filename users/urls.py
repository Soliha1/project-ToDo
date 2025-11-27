from django.urls import path
from .views import *
urlpatterns=[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]