from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.
def create_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = forms.AlbumForm()
    return render(request, 'album.html', {'form': form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'album.html', {'form': form})


def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('profile')