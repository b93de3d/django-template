from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import core.serializers as core_serializers
import core.models as core_models
from util import admin_send_email
from {{ project_name }}.settings import EMAIL_HOST_USER, DEBUG_EMAIL


class TokenLogin(ObtainAuthToken):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ExampleViewSet(DynamicModelViewSet):
    serializer_class = core_serializers.Example
    queryset = core_models.Example.objects.all()


@api_view(["GET"])
@permission_classes([])
def ping(request):
    admin_send_email([DEBUG_EMAIL], "It works!", "Nice")
    return Response({"message": "pong"}, status=status.HTTP_200_OK)
