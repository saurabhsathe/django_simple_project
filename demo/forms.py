# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe


class userChoiceForm(forms.Form):
    option1=("no","no")
    option2=("yes","Yes")
    
    your_name = forms.CharField(label='Your name', max_length=100)
    choice1=forms.ChoiceField(label="option 1 ", choices=[option1,option2])
    
    
    