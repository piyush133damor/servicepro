from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('service_list',views.service_list_view, name="service_list"),
    path('brand_service_list',views.brand_service_list_view, name="brand_service_list"),
    path('servicecenter_detail/<int:pk>',views.servicecenter_detail_view, name="servicecenter_detail_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('servicecenter_review/<int:no>',views.servicecenter_review, name="servicecenter_review"),
    path('servicecenter_list_review/<int:pk>',views.servicecenter_review_list, name="servicecenter_review_list"),


]