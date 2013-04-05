# Create your views here.
from formpost.models import uPost
from formpost.serializers import FormSerializer
from rest_framework import generics 
class uPostlist(generics.ListCreateAPIView):
	model = uPost
	serializer_class = FormSerializer

class uPostDetail(generics.RetrieveUpdateDestroyAPIView):
	model= uPost
	serializer_class = FormSerializer


