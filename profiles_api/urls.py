from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # start DRF 3.9 version and later, base_name argument has been renamed in favor to basename.
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),

    # path('profile/', views.UserProfileApiView.as_view()),  # my code using APIView
    # path('profile/<int:pk>', views.UserProfileApiView.as_view()),  my code using APIView
]
