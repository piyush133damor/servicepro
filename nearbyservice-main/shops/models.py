from djgeojson.fields import PointField
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import  get_object_or_404


import decimal
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
# from django_postgres_extensions.models.fields import ArrayField, ArrayManyToManyField

class Item(models.Model):
    # chef = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    brand_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)    
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='item_pics')


    def __str__(self):
        return self.brand_name + " "+ self.model_no

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Item.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', kwargs={
            'slug': self.slug
        })





    
    



class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300, default=' ')
    shop_owner= models.CharField(max_length=100,blank=True)
    owner_email= models.CharField(max_length=100,blank=True)
    location = models.PointField(null=True,blank=True, spatial_index=True, geography=True)
    lattitude=models.DecimalField(max_digits=20, decimal_places=10,default=decimal.Decimal(0))
    longitude=models.DecimalField(max_digits=20, decimal_places=10,default=decimal.Decimal(0))
    brand_service_available = ArrayField(models.CharField(max_length=200), blank=True, default=[''])
    cover_image=models.ImageField(blank=True,null=True,upload_to="covers/%Y/%M/%D")
    image_with_Aadhar=models.ImageField(upload_to="aadhar/%Y/%M/%D", default="../media/aadhar/woman-holding-identification-card-CTYYDW.jpg")
    is_published = models.BooleanField(default=False) 
    list_date=models.DateTimeField(default=datetime.now(),blank=True)
   


    def __str__(self):
        return self.name

    def update(self, str):
        self.brand_service_available.append(str)

    def empty(self):
        while len(self.brand_service_available) > 0 : self.brand_service_available.pop()

class Review(models.Model):
    shop_pk = models.IntegerField(default=11)
    customer = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_review = models.BooleanField(default=False) 
    service_no = models.IntegerField(max_length=100, default=10000)
    

    def approve(self):
        self.approved_review = True 
        self.save()

    def __str__(self):
        return self.text




class Serviceable_list_items(models.Model):
    shop = models.ForeignKey(Shop,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestampStr = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    
    def __str__(self):
        return f"{self.user} of {self.item}"
    
    

    