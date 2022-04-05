from typing import Type, Callable, Any

from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.serializers import Serializer

from {{ project_name }}.settings import EMAIL_HOST_USER


def validate_array(unknown: Any) -> None:
    if type(unknown) != list:
        raise ValidationError("This field should be an array.")


def get_or_none(model: Type[models.Model], **kwargs) -> Type[models.Model]:
    """
    Object from Model.objects.get(**kwargs) or None
    """
    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise ValidationError({"error": [f"object not found: {model} {kwargs}"]})
    return obj


def get_request_data(
    request: Request, key: str, default: Any = None, validate: Callable = None
) -> Any:
    """
    Get item from request data by key, raising a ValidationError if
    data is not present. Optionally applies validation function.
    Validation function should raise its own validation errors.
    """
    data = request.data.get(key, default)
    if data is None:
        raise ValidationError({key: ["This field is required."]})
    if validate is not None:
        validate(data)
    return data


def serialize_and_validate(data: dict, serializer: Type[Serializer]) -> dict:
    """
    Raises ValidationError if missing or invalid field(s)
    """
    serialized = serializer(data=data)
    serialized.is_valid(raise_exception=True)
    return serialized.data


def get_data_serializer_validated(
    request: Request, serializer: Type[Serializer]
) -> dict:
    """
    Relies on serializer to take all the fields it needs from the
    request data.
    """
    return serialize_and_validate(request.data, serializer)


def get_array_serializer_validated(
    request: Request, key: str, serializer: Type[Serializer]
) -> list[dict]:
    """
    Gets user submitted array and then relies on the serializer to
    take all the fields it needs from the array items.
    """
    data_array = get_request_data(request, key, validate=validate_array)
    return [serialize_and_validate(data, serializer) for data in data_array]


def admin_send_email(recipient_list, subject, message, html_template=None, html_context=None):
    send_mail(
        from_email=f'"{{ project_name }}" <{EMAIL_HOST_USER}>',
        recipient_list=recipient_list,
        subject=subject,
        message=message,
        html_message=render_to_string(
            template_name=html_template, context=html_context
        ) if html_template else None,
    )
