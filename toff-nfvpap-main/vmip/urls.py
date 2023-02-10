from django.urls import path

from . import views

urlpatterns = [
    path('', views.statistics, name='statistics'), #漁船進出港統計頁面
    path('gis', views.gis, name='gis'), #漁船地圖視覺化頁面
    path('boat_details', views.boat_details, name='boat_details'), #漁船詳細資料頁面
    path('register', views.register, name='register'), #漁港管理註冊頁面
    path('login', views.login, name='login'), #漁港管理登入頁面
    path('idle-statistics', views.idle_statistics, name='idle_statistics'), #船舶閒置統計頁面
    path('edit-comment', views.edit_comment, name='edit_comment'), #船舶閒置統計頁面
]