from  django import forms
from .models import *


class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields='__all__'


class NoticeForm(forms.ModelForm):
	class Meta:
		model=Notice
		fields='__all__'