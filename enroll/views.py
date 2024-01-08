# views.py
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a generic success URL after a successful form submission
            return redirect('home')
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, 'enroll/home.html', {'img': img, 'form': form})
