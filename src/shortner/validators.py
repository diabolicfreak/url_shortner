from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()

    value_1_valid = False
    value_2_valid = False

    try:
        url_validator(value)
    except:
        value_1_valid = True

    value_2 = "http://"+value
    try:
        url_validator(value_2)
    except:
        value_2_valid = True

    if value_1_valid and value_2_valid:
        raise ValidationError("invalid url for this field")

    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("Not valid because no .com")
    return value
