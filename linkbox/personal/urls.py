from django.conf.urls import url
from personal import views


app_name = 'personal'
urlpatterns = [
    url(r'^users/$', views.UserView.as_view(), name='user_list'),
    url(r'^users/(?P<username>[\w]+)/$', views.UserInstanceView.as_view(),
        name='user_instance'),
]
