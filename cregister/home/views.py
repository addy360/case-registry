from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ClientIssues, CaseType
def index(request):
	caseTypes = CaseType.objects.all()
	issues = ClientIssues.objects.all()
	context = {
		'caseTypes': caseTypes,
		'issues': issues,
	}
	return render(request, 'home/home.html', context)

def issue(request):
	if request.method == 'POST':
		iss = request.POST['issueType']
		if iss == '':
			messages.add_message(request, messages.ERROR, 'Please enter something!')
		else:		
			ClientIssues.objects.create(name=iss)
			messages.add_message(request, messages.SUCCESS, f'You have added "{iss}" successfully!')
	return redirect('/')

def caseType(request):
	if request.method == 'POST':
		iss = request.POST['caseType']
		if iss == '':
			messages.add_message(request, messages.ERROR, 'Please enter something!')
		else:		
			CaseType.objects.create(name=iss)
			messages.add_message(request, messages.SUCCESS, f'You have added "{iss}" successfully!')
	return redirect('/')


