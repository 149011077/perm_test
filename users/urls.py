from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'users/$', views.users, name='users'),
    url(r'add_user/$', views.add_user, name='add_user'),
    url(r'edit_user/$', views.edit_user, name='edit_user'),
]