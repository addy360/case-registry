from django.shortcuts import render

def client_form(request):
	return render(request, 'client/client.html')