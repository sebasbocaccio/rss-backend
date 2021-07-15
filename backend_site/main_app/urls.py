from django.urls import path
from main_app import views
from django.conf.urls import url
from django.contrib import admin
from .views.register import RegisterApi
from .views.login import LoginAPIView
from .views.subscription_feed import CreateSubscriptionFeedAPI

urlpatterns = [
    path('register/', RegisterApi.as_view(), name=''),
    path('login/',LoginAPIView.as_view(),name=''),
    path('create_feed/', CreateSubscriptionFeedAPI.as_view(),name='createdFeed')
]
