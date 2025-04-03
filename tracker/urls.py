from django.urls import path
from tracker.views import index,deletetransaction
urlpatterns = [
    path('', index , name='index'),
    path('delete-transaction/<uuid>', deletetransaction , name='deletetransaction'),
]
