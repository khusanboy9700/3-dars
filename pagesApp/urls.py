from django.urls import path
from .views import HomePageView, AboutPageView, NewPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('news/', NewPageView.as_view(), name='news'),
]
