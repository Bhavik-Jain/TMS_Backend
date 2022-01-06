from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from api.views import *
from django.conf.urls.static import static
from django.conf import settings
from api import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)), 

    path('profile/<int:id>', views.ProfileDetailAPIView.as_view(), name="profile"),

    path('packages/', views.PackagesListAPIView.as_view(), name="packages"),
    path('packages/<int:id>', views.PackagesDetailAPIView.as_view()),

    path('bookings/', views.BookingsListAPIView.as_view()),
    path('bookings/<int:id>', views.BookingsDetailAPIView.as_view()),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)