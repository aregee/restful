from django.db import models
import datetime

# Create your models here.
class uPost(models.Model):
	title = models.CharField(max_length=146)
	body = models.CharField(max_length=1500)
	author = models.CharField(max_length=40)
	location = models.CharField(max_length=134)
	pub_date = models.DateTimeField(auto_now_add=True)
	
#	def __unicode__(self):
#		return (self.body)

#	def get_author_url(self):
#		return "/u/%s/p/0" % (self.author)
	
	class Meta:

		ordering = ['-pub_date']
