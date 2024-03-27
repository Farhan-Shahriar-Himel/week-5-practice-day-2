from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = forms.MusicianForm()
    return render(request, 'musician.html', {'form': form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'musician.html', {'form': form})


def delete_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('profile')
