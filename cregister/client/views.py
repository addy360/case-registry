from django.shortcuts import render

from home.models import ClientIssues
def client_form(request):
	issues = ClientIssues.objects.all()
	context = {
		'issues' : issues
	}
	return render(request, 'client/client.html', context)