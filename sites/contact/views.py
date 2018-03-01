from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            response = HttpResponse()
            response.write("<h1>Thanks you foe register</h1></br>")
            return response 
    else:
        form = ContactForm()
    return render(request, 'contact/home.html',{'form':form})  