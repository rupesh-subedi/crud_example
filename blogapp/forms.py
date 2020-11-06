from django import forms
from django.forms import ModelForm
from .models import *


class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__"
		