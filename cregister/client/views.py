from django.shortcuts import render, redirect
from django.contrib import messages

from home.models import ClientIssues
from .models import Client
def client_form(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		mname = request.POST['mname']
		lname = request.POST['lname']
		caseNo = request.POST['caseNo']
		phone = request.POST['phone']
		issueId = request.POST['issueId']
		print(issueId)
		if fname == '' or mname == '' or lname == '' or caseNo == '' or phone == '' or issueId == '':
			messages.add_message(request, messages.ERROR, f'All fields must be filled!')
			return redirect('client')
		client_instance = ClientIssues.objects.get(id=issueId)
		client = Client(first_name=fname, middle_name = mname, last_name = lname, case_no =caseNo, phone = phone, issue = client_instance)
		client.save()
		messages.add_message(request, messages.SUCCESS, f'Client saved successfully. Add client\'s case!')
		return redirect('case')
	else:
		issues = ClientIssues.objects.all()
		context = {
			'issues' : issues
		}
		return render(request, 'client/client.html', context)