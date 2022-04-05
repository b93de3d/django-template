from django.urls import path
from dynamic_rest.routers import DynamicRouter
import core.views as core_views

router = DynamicRouter()
router.register("examples", core_views.ExampleViewSet)

urlpatterns = router.urls + [
    path("login", core_views.TokenLogin.as_view(), name="login"),
    path("ping", core_views.ping, name="ping"),
]
