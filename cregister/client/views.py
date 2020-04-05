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
	clientOb = Client.objects.get(id=id)
	client = {}
	client['full_name'] = f'{clientOb.first_name} {clientOb.middle_name} {clientOb.last_name}'
	client['case_no'] = clientOb.case_no 
	client['phone'] = clientOb.phone 
	client['issue'] = clientOb.issue.name 
	cases = [] 
	context = {
		'full_name':client['full_name'],
		'case_no':client['case_no'],
		'phone':client['phone'],
		'issue':client['issue'],
		'cases':cases,
	}
	for case in clientCases:
		category = case.case_types.values()[0]['name']
		judge = case.judge
		advocate = case.advocate
		against = case.against
		created_at = case.created_at
		# print(f'{category} {judge} {advocate} {against} {created_at}')
		cases.append([category,against,judge,advocate,created_at])


	return render(request, 'client/client-details.html', context)