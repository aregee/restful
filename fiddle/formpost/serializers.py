from django.forms import widgets 
from rest_framework import serializers
from formpost.models import *

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = uPost
        fields = ('id','title','body','author','location','pub_date')

    def restore_object(self, attrs,instance=None):
        if instance:
            instance.title=attrs.get('title',instance.title)
	    instance.body = attrs.get('body',instance.body)
	    instance.author=attrs.get('author',instance.author)
            instance.location=attrs.get('location',instance.location)
            instance.pub_date=attrs.get('pub_date',instance.pub_date)
        return uPost(**attrs)

