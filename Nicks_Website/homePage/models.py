from django.db import models

#choices
job_Position_Choices = (
	("- Postion -", "- Postion -"),
	("Internship", "Internship"),
	("Part-Time", "Part-time"),
	("Full-Time", "Full-time"),
	)

# Create your models here.
class Company_Application(models.Model):
	company_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	location = models.CharField(max_length=100)
	company_website = models.URLField(max_length=100)
	hiring_position = models.CharField(max_length=100)
	description = models.TextField()
	position_type = models.CharField(max_length = 20, choices = job_Position_Choices, default = '- Postion -')