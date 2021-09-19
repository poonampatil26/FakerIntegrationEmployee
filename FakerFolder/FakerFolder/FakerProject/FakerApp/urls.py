from django.urls import path
from .views import fakeDataView

urlpatterns = [
    path('fake/', fakeDataView)
]