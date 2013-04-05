from django.forms import ModelForm

from formpost.models import * 

class PostForm(ModelForm):
	
	class Meta:
	  model = uPost
	  exclude = ['pub_date']


