from django.urls import path
from . import views


urlpatterns = [
    path('thank-you/', views.newsletter, name='newsletter')
]
