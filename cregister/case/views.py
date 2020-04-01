from django.shortcuts import render

def case_form(request):
	return render(request,'case/case.html')