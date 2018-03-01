from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from django.utils import timezone
from .forms import MyCommentForm
def add_model(request):
 
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
 
    else:
 
        form = MyCommentForm()
 
        return render(request, "my_template.html", {'form': form})
