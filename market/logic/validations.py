from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def check_email(email):

    try:
        validate_email(email)
    except ValidationError as e:
        return False
    else:
        return True


def check_password(password):
    if len(password) < 8:
        return False
    else:
        return True