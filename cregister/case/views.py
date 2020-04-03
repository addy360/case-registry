from django.shortcuts import render, redirect
from django.contrib import messages

from home.models import CaseType
from client.models import Client
from .models import Case
def case_form(request):
	if request.method == 'POST':
		clientId = request.POST['clients']
		against = request.POST['against']
		judge = request.POST['judge']
		advocate = request.POST['advocate']
		case_typeId = request.POST['case_types']
		if clientId == '' or against == '' or judge == '' or advocate == '' or case_typeId == '':
			messages.add_message(request, messages.ERROR, 'All fields are required!')
			return redirect('case')
		client = Client.objects.get(id=clientId)
		case_type = CaseType.objects.get(id=case_typeId)
		case = Case(against=against, judge = judge, advocate=advocate)
		case.save()
		case.clients.add(client)
		case.case_types.add(case_type)
		case.save()
		messages.add_message(request, messages.SUCCESS, 'Case saved successfully!')
		return redirect('home')
	else:
		caseTypes = CaseType.objects.all()
		clients = Client.objects.all()
		context = {
			'caseTypes': caseTypes,
			'clients': clients,
		}
		return render(request,'case/case.html', context)