import sys
sys.path.append("..")

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from shops import views
from django.conf import settings
from django.views.static import serve
from djgeojson.views import GeoJSONLayerView
from shops.models import Shop
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name = 'register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'shops/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'shops/index.html'), name = 'logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('',include('shops.urls')),
]





if settings.DEBUG:
    urlpatterns+=[
        url(r'^media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT
        }),
    ]