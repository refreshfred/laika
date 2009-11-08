from django.db import models

class Slide(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField(blank = True)
	slug = models.SlugField()
	status_modes = (
		(0, 'Draft'),
		(1, 'Published'),
	)
	status = models.IntegerField(choices = status_modes, default = 0)
	
	# Override the default string setup, so any time a string representation of this is called (admin), we return the title
	def __str__(self):
		return "%s" % self.title
