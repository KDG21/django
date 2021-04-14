from django.urls import path
from pose.views import PoseCheckView

urlpatterns = [
    path("pose/", PoseCheckView.as_view()),
]