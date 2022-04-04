from dynamic_rest.serializers import DynamicModelSerializer
import core.models as core_models


class Example(DynamicModelSerializer):
    class Meta:
        model = core_models.Example
        exclude = []
