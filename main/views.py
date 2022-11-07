from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main(request):
	return render(request, 'main/main.html')


def login(request):
	return render(request, 'main/login.html')
def signup(request):
	return render(request, 'main/signup.html')