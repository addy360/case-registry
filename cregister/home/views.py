from django.shortcuts import render

from .models import ClientIssues, CaseType
def index(request):
	caseTypes = CaseType.objects.all()
	issues = ClientIssues.objects.all()
	context = {
		'caseTypes': caseTypes,
		'issues': issues,
	}
	return render(request, 'home/home.html', context)