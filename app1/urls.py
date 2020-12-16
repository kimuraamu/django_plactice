from django.urls import path

from .views import indexView,aboutView

urlpatterns = [
    path('', indexView.as_view()),
    path('about/', aboutView.as_view()),
]