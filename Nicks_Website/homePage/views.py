from django.shortcuts import render, redirect
from .models import Company_Application
from .forms import Company_ApplicationForm
from django.contrib import messages

# Create your views here.
def index(request):

	form = Company_ApplicationForm()

	if request.method == 'POST':
		form = Company_ApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')

	context = {'form': form}
	return render(request, 'index.html', context)
