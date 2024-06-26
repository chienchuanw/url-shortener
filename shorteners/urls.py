from django.urls import path
from .views import ShortenerHomeView

app_name = "shorteners"

urlpatterns = [
    path(
        "",
        ShortenerHomeView.as_view(),
        name="home",
    )
]
