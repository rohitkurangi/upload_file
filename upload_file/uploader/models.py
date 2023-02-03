from django.db import models

class Upload(models.Model):
	upload_file = models.FileField()    
	upload_date = models.DateTimeField(auto_now_add =True)

	def __str__(self):
		return "{0}".format(self.upload_file)


class UploadFile(models.Model):
	file = models.FileField(upload_to='documents/',null=True)
	upload_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0}".format(self.file)