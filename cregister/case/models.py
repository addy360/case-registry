from django.db import models

from client.models import Client
from home.models import CaseType

class Case(models.Model):
	clients = models.ManyToManyField(Client)
	case_types = models.ManyToManyField(CaseType) 
	against = models.CharField(max_length=50)
	judge = models.CharField(max_length=50)
	advocate = models.CharField(max_length=50)
	# created_at	 = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.against