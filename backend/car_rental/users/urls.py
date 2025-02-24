from django.urls import path

from users import views


urlpatterns = [
    path('user/', views.get_user_page, name='user page'),
    path('userinfo/<str:name>', views.get_user_info, name='user name'),
    path('userage/', views.get_user_age, name='user age')
]
