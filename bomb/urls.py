from django.urls import path
from .views import *

urlpatterns = [
    path("", all, name="all"),
    path("create/", create, name="create"),
    path("update/<int:id>", update, name="update")
]