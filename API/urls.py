from django.urls import path
from . import views
from .views import RecentLinkView
app_name = "API"

urlpatterns = [
    path("", RecentLinkView.as_view(), name="recent_link"),
]
