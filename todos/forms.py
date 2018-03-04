from django import forms
from django.contrib.auth.models import User
from .models import *
class PredictForm(forms.ModelForm):
    month=forms.IntegerField(help_text="Please enter which month you start to rent")
    bedroom=forms.IntegerField(help_text="Please enter how many bedrooms your want")

    MAJOR_CHOICES = (
        ('Near School', 'Near School'),
        ('Far from School', 'Far from School'),)
    distance=forms.ChoiceField(choices=MAJOR_CHOICES,help_text="Please choose the distance to school")
    class Meta:
        model=House
        fields = ('month', 'bedroom', 'distance')

class PostForm(forms.ModelForm):
    text=forms.CharField(help_text="Please leave your message for renting")
    class Meta:
        model=Post
        fields=('text',)