from django.urls import path
from .views import SignUpView, homePageView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
