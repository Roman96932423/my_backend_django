from django.urls import path

from users.views import get_user_page, get_user_info, get_user_age


urlpatterns = [
    path('', get_user_page, name='user page'),
    path('userinfo/<str:name>', get_user_info, name='user name'),
    path('userage/', get_user_age, name='user age')
]
