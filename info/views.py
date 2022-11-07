from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mycar(request):
	return render(request, 'info/mycar.html')

