from django.urls import path
from .views import SignUpView, ResendActivationView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_signup'),
    path('resend/', ResendActivationView.as_view(), name='user_resend')
]
