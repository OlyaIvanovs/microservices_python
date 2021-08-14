from django.urls import path
from .views import ProductViewSet, UserAPIView


urlpatterns = [
    path("products", ProductViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "products/<str:pk>",
        ProductViewSet.as_view(
            {"put": "update", "delete": "destroy", "get": "retrieve"}
        ),
    ),
    path("user", UserAPIView.as_view()),
]
