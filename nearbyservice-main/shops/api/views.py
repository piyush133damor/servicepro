from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from shops.models import Shop, Review
from .serializers import ShopSerializer, ShopSerializerAbstract, ReviewSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance as dist
from django_postgres_extensions.models.functions import *
import decimal
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import render, get_object_or_404

from django.db.models import Q
@api_view(http_method_names=['GET',])
@permission_classes([IsAuthenticated])
def service_list_view(request):
    radius = 5
    user_location = Point(0, 0, srid=4326)
    query=""
    

    try:
        
        longitude=float(request.GET['long'])
        latitude=float(request.GET['lat'])
        shops =[]

        user_location = Point(longitude, latitude, srid=4326)
        print(user_location)

        while not shops:
            if radius>300:
                break
            radius+=5
            shops_within_radius=Shop.objects.filter(location__distance_lt=(user_location, dist(km=radius))) 

            if shops_within_radius:
                shops = shops_within_radius.annotate(distance=Distance('location',
                user_location)
                ).order_by('distance')

                
        serializer = ShopSerializerAbstract(shops,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    











@api_view(http_method_names=['GET',])
@permission_classes([IsAuthenticated])
def brand_service_list_view(request):
    radius = 5
    user_location = Point(0, 0, srid=4326)
    query=""
    

    try:
        query=request.GET['b'] + " "+ request.GET['m']
        longitude=float(request.GET['long'])
        latitude=float(request.GET['lat'])
        shops =[]

        user_location = Point(longitude, latitude, srid=4326)
        print(user_location)

        while not shops:
            if radius>300:
                break
            radius+=5
            shops_within_radius=Shop.objects.filter(location__distance_lt=(user_location, dist(km=radius))) 

            if shops_within_radius:
                shops = shops_within_radius.annotate(distance=Distance('location',
                user_location)
                ).order_by('distance')

                shops=shops.filter(brand_service_available__contains=[query]).distinct()
        serializer = ShopSerializerAbstract(shops,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    



@api_view(http_method_names=['GET',])
def servicecenter_detail_view(request, pk):
    try:
        hdata = Shop.objects.get(pk=pk)
        if request.method == 'GET':
            return servicecenter_detail_view_get(request, pk, hdata)
        
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def servicecenter_detail_view_get(request, pk, hdata):
    serializer = ShopSerializer(hdata)
    return Response(serializer.data)



@api_view(http_method_names=['GET'])
def servicecenter_review_list(request, pk):
    try:
        hdata = Review.objects.filter(shop_pk=pk)
        serializer = ReviewSerializer(hdata, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=['GET','PUT','DELETE'])
def servicecenter_review(request, no):
    try:
        
        hdata = Review.objects.get(service_no=no)
        if request.method == 'GET':
            return servicecenter_review_get(request, no, hdata)
        elif request.method == 'PUT':
            return servicecenter_review_put(request, no, hdata)
        elif request.method == 'DELETE':
            return servicecenter_review_delete(request, no, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def servicecenter_review_get(request, no, hdata):
    serializer = ReviewSerializer(hdata)
    return Response(serializer.data)

def servicecenter_review_put(request, no, hdata):
    serializer = ReviewSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def servicecenter_review_delete(request, no, hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    return Response(data)
    

    