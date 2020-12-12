from django.urls import path
from . import views
from django.conf.urls import url, include
from mysite import settings
from django.views.static import serve 

urlpatterns = [
    path('servicelist/<int:pk>/', views.service_list , name='service_list'),
    path('menu/<int:pk>/', views.menu , name='menu'),
    path('', views.shop_list,name='home'),
    path('shop/new/', views.shop_new, name='shop_new'),
    path('myshops/', views.myshops, name='myshops'),
    path('shop/<int:pk>/', views.shop_detail, name='shop_detail'),
    path('shop/<int:pk>/edit/', views.shop_edit, name='shop_edit'),
    path('shop/<pk>/remove/', views.shop_remove, name='shop_remove'),
    path('shop/<int:pk>/review/', views.add_review_to_shop, name='add_review_to_shop'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('order', views.order, name='order'),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('add-to-cart/<slug>/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('servicelisttoarray/<int:pk>/', views.returnArray, name= 'servicelisttoarray'),
    path('remove-from-cart/<slug>/<int:pk>/', views.remove_from_cart, name= 'remove-from-cart'),
    path('api/', include('shops.api.urls')),
]