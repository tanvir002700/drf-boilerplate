from django.urls import path
from .views import (SignUpView, ResendActivationView, ActivationView,
                    LoginView, LogoutView, SetPasswordView, SetUserEmailView,
                    PasswordResetView, PasswordResetConfirmView)


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_signup'),
    path('resend/', ResendActivationView.as_view(), name='user_resend'),
    path('activate/', ActivationView.as_view(), name='user_activate'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('set_password/', SetPasswordView.as_view(), name='set_password'),
    path('set_email/', SetUserEmailView.as_view(), name='set_email'),
    path('reset_password/', PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_confirm/', PasswordResetConfirmView.as_view(),
         name='reset_password_confirm')
]
