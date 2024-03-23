from django.contrib import admin
from django.urls import path
from rest_framework import routers

from movies.views import MovieViewSet, DirectorViewSet

router = routers.SimpleRouter()
router.register(r"movies", MovieViewSet)
router.register(r"directors", DirectorViewSet)
urlpatterns = router.urls
