from django.urls import path, include
from .views import *

urlpatterns = [
    path('send-otp/', SendOtp.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOtp.as_view(), name='verify-otp'),
    path('signup/', Login.as_view(), name='login'),
]