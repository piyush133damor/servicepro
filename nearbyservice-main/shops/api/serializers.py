from rest_framework import serializers
from shops.models import Shop, Review


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'shop_owner', 'location', 'lattitude', 'longitude', 'brand_service_available']


class ShopSerializerAbstract(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'location', 'lattitude', 'longitude', 'pk']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['shop_pk','customer','text', 'created_date']






# class ShopSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     address = serializers.CharField(max_length=300)
#     shop_owner= serializers.CharField(max_length=100)
#     owner_email= serializers.CharField(max_length=100)
#     location = serializers.PointField(null=True,blank=True, spatial_index=True, geography=True)
#     lattitude=serializers.DecimalField(max_digits=20, decimal_places=10,default=decimal.Decimal(0))
#     longitude=serializers.DecimalField(max_digits=20, decimal_places=10,default=decimal.Decimal(0))
#     brand_service_available = ArrayField(models.CharField(max_length=200), blank=True, default=[''])
#     cover_image=serializers.ImageField()
#     image_with_Aadhar=serializers.ImageField()
#     is_published = serializers.BooleanField(default=False) 
#     list_date=serializers.DateTimeField(default=datetime.now())
#     # hid = serializers.CharField(max_length=16)
#     # address = serializers.CharField()
#     # adults = serializers.IntegerField()
#     # children = serializers.IntegerField()
#     # earners = serializers.IntegerField()
#     # income = serializers.FloatField()
#     # enteredBy = serializers.SlugRelatedField(read_only= True, slug_field='username')

#     def create(self, validated_data):
#         return HouseholdData(**validated_data)

#     def update(self, instance, validated_data):
#         instance.hid = validated_data.get('hid', instance.hid)
#         instance.address = validated_data.get('address', instance.address)
#         instance.adults = validated_data.get('adults', instance.adults)
#         instance.children = validated_data.get('children', instance.children)
#         instance.earners = validated_data.get('earners', instance.earners)
#         instance.income = validated_data.get('income', instance.income)
#         instance.save()
#         return instance  