from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework import exceptions as drf_exceptions

from djoser import utils
from djoser.conf import settings
from config import exceptions

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            'email',
            'password',
        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get('password')

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            messages = [_(message) for message in e.messages]

            raise serializers.ValidationError({'password': messages})

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            raise exceptions.AlreadyExists(
                _('The provided email address already has an account.'))

        return user

    @staticmethod
    def perform_create(validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=['is_active'])
        return user


class EmailAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        users = self.context['view'].get_users(value)
        if not users:
            raise drf_exceptions.NotFound(
                _('User account with given email does not exist.'))
