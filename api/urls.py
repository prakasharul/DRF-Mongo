from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'users$', views.UserViewSet.as_view({'get':'list'}), name='user_list'),
    re_path(r'users/create$', views.UserViewSet.as_view({'post': 'create'}), name="user_create"),
    re_path(r'users/(?P<pk>[\w-]+)$', views.UserViewSet.as_view({'get':'retrieve'}), name="user_detail"),
    re_path(r'users/(?P<pk>[\w-]+)/update$', views.UserViewSet.as_view({'post':'update','get':'retrieve'}), name='user_update'),
    re_path(r'users/(?P<pk>[\w-]+)/delete$', views.UserViewSet.as_view({'delete':'delete','get':'retrieve'}), name="user_delete")
]
