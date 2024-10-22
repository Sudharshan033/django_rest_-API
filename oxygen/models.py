from django.db import models
class project_details(models.Model):
	projectname=models.CharField(max_length=50)
	objective=models.CharField(max_length=50)
	studentname=models.CharField(max_length=40)
	department=models.CharField(max_length=40)
