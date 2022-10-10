from django.urls import path
from start_page.views import page

urlpatterns = [ 
    path('', page, name='page'),
]