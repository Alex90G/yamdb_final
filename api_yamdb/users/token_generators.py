from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import AccessToken


def generate_key(user):
    """Генератор кода подтверждения"""
    return default_token_generator.make_token(user)


def get_tokens_for_user(user):
    """Генератор аксесс-токена JWT."""
    #access = AccessToken.for_user(user)

    return AccessToken.for_user(user)
