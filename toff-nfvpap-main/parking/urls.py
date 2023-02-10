from django.urls import path

from . import views

urlpatterns = [
    path('apply', views.apply, name='apply'),
    path('history', views.history, name='history'),
    path('payment', views.payment, name='payment'), # 繳費頁面
    path('calculate-payment', views.calculate_payment, name='calculate_payment'), # 預計繳費頁面
    path('parkings', views.parkings, name='parkings'),
    path('review', views.review, name='review'),
    path('berth-review', views.berth_review, name='berth_review'), #泊位審核頁面
    path('berth-view', views.berth_view, name='berth_view'), #審核檢視頁面
    path('statistics', views.statistics, name='statistics'),
    path('admin-apply', views.admin_apply, name='admin_apply'),
    path('news-list', views.news_list, name='news_list'), #後臺公告列表頁面
    path('new-edit/1', views.new_edit, name='new_edit'), #公告編輯頁面
    path('create-new', views.create_new, name='create_new'), #公告新增頁面
    path('add-new-type', views.add_new_type, name='add_new_type'), #公告類別新增頁面
    path('add-nocharge-reason', views.add_nocharge_reason, name='add_nocharge_reason'), #不收費原因新增頁面

    path('payment-admin', views.payment_admin, name='payment_admin'), # 費用管理 - 繳費紀錄
    path('payment-refund', views.payment_refund, name='payment_refund'), # 費用管理 - 退費/註銷繳費單
    path('refund', views.refund, name='refund'), # 費用管理 - 退費
    path('not-applied', views.not_applied, name='not_applied'), # 費用管理 - 退費/註銷繳費單
    path('not-applied/review', views.not_applied_review, name='not_applied_review'), # 費用管理 - 退費/註銷繳費單
    path('ajax/load-ports', views.load_ports, name='ajax_load_ports'),
    path('ajax/load-vessels', views.load_vessels, name='ajax_load_vessels'),
]