from django.urls import path
from users.views import page

urlpatterns = [
    path('', page, name='page'),
]