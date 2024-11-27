from django.urls import path
from .views import user_list_create, user_detail, login_user

urlpatterns = [
    path('users/', user_list_create, name='user-list-create'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('login/', login_user, name='login'),
]
