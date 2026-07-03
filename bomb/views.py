from django.shortcuts import render, redirect
from .forms import View
from .models import Customers


def all(request):
    info = Customers.objects.all()
    return render(request, "all.html", {"info": info})


def create(request):
    form = View(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('all')

    return render(request, 'create.html', {'form': form})


def update(request, id):
    student = Customers.objects.get(id=id)
    form = View(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('all')

    return render(request, 'create.html', {'form': form, 'student': student})


