from django.shortcuts import render


from home.models import CaseType
def case_form(request):
	caseTypes = CaseType.objects.all()
	context = {
		'caseTypes': caseTypes
	}
	return render(request,'case/case.html', context)