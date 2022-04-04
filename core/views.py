from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

import core.serializers as core_serializers
import core.models as core_models


class ExampleViewSet(DynamicModelViewSet):
    serializer_class = core_serializers.Example
    queryset = core_models.Example.objects.all()


@api_view(["GET"])
@permission_classes([])
def ping(request):
    if len(request.data.keys()) > 0:
        raise ValidationError({"data": ["This endpoint does not accept any data."]})
    return Response({"message": "pong"}, status=status.HTTP_200_OK)
