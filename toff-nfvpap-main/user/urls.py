from django.urls import path

from . import views
from .views import RegisterView

urlpatterns = [
    # path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('news-list', views.news_list, name='news_list'), #最新公告列表頁面
    path('new', views.new, name='new'), #公告頁面
    path('register', RegisterView.as_view(), name='register'), #註冊頁面
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
]