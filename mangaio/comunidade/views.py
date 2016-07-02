from django.shortcuts import render
from comunidade.models import UserProfile

# Create your views here.
def index(request):
	
	profiles = UserProfile.objects.all()

	return render(request, 'comunidade/index.html', {'profiles':profiles})