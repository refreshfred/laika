from django.db import models

class Slide(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(blank=True)
	status_modes = (
		(0, 'Draft'),
		(1, 'Published'),
	)
	status = models.IntegerField(choices = status_modes, default=0)
