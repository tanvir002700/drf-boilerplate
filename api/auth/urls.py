from django.urls import path
from .views import SignUpView, ResendActivationView, ActivationView, LoginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_signup'),
    path('resend/', ResendActivationView.as_view(), name='user_resend'),
    path('activate/', ActivationView.as_view(), name='user_activate'),
    path('login/', LoginView.as_view(), name='user_login')
]
