from django.urls import path

from . import views


urlpatterns = [
    path('graphql', views.test_graphql),
]
