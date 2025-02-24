from django.urls import path

from cars import views


urlpatterns = [
    path('', views.get_view, name='home page'),
    path('argument/<str:arg>', views.get_view_with_arg, name='argument page'),
    path('parametr/', views.get_view_with_param, name='parametr page')
]