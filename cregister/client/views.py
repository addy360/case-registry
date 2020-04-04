from django.shortcuts import render, redirect
from django.contrib import messages

from case.models import Case
from home.models import ClientIssues, CaseType
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
		messages.add_message(request, messages.SUCCESS, f'{fname} saved successfully!')
		return redirect('home')
	else:
		issues = ClientIssues.objects.all()
		context = {
			'issues' : issues
		}
		return render(request, 'client/client.html', context)

def client_details(request, id):
	clientCases = Case.objects.prefetch_related('case_types').filter(clients=Client.objects.get(id=id))
	client = Client.objects.get(id=id)
	cases = [{'client':client}]
	for case in clientCases:
		name = case.case_types.values()[0]['name']
		cases.append({'case':case,'case_types': name})
	print(cases)
	context = {
		'cases':cases
	}
	return render(request, 'client/client-details.html', context)