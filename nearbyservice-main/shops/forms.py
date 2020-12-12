from django import forms
from .models import Shop, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.postgres.forms import SimpleArrayField

class PostForm(forms.ModelForm):

    class Meta:
        model = Shop
        brand_service_available = SimpleArrayField(forms.CharField())
        fields = ('name', 'lattitude','longitude','cover_image','image_with_Aadhar', 'address')

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('customer', 'text',) 

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	contact = forms.CharField()

	class Meta:
		model = User
		fields = ['username', 'email', 'contact', 'password1', 'password2']

