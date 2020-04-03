from django.db import models
from datetime import datetime

from home.models import ClientIssues
class Client(models.Model):
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	case_no = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	issue = models.ForeignKey(ClientIssues,  on_delete=models.DO_NOTHING)
	created_at	 = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.first_name 