from django.urls import path
from tracker.views import index,deletetransaction,registration,login_page,logout_page
urlpatterns = [
    path('', index , name='index'),
    path('delete-transaction/<uuid>', deletetransaction , name='deletetransaction'),
    path('registration/', registration , name='registration'),
    path('logout/', logout_page , name='logout_page'),
    path('login/', login_page , name='login_page'),
]
