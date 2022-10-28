from django.core import exceptions
from django.shortcuts import render, redirect

from ExamPreparationMusic.music.forms import ProfileCreateForm, AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from ExamPreparationMusic.music.models import Profile, Album


# Create your views here.

def get_profiles():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None

def index(request):
    contex={}
    profile = get_profiles()
    if profile is None:

        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
                profile = Profile.objects.get()
            return redirect('index')
        else:
            form = ProfileCreateForm()
            contex = {
                'form': form
        }

        return render(request, 'core/home-no-profile.html', contex)

    profile = Profile.objects.get()
    contex['profile'] = profile
    contex['albums'] = Album.objects.all()

    return render(request, 'core/home-with-profile.html', contex)



def add_album(request):
    contex = {}
    if request.method == 'POST':
        form = AlbumAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumAddForm()

        contex['form'] = form

    return render(request, 'albums/add-album.html', contex)

def details_album(request, pk):
    contex = {}
    album = Album.objects.filter(pk=pk).get()
    contex['album'] = album

    return  render(request, 'albums/album-details.html',contex)

def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    contex = {}
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumEditForm(instance=album)

    contex['form'] = form
    contex['album'] = album
    return  render(request, 'albums/edit-album.html', contex)

def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    contex = {}
    if request.method == 'POST':
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = AlbumDeleteForm(instance=album)

    contex['form'] = form
    contex['album'] = album

    return render(request, 'albums/delete-album.html', contex)


def details_profile(request, pk):

    return  render(request, 'profiles/profile-details.html')


def delete_profiles(request):
    return  render(request, 'profiles/profile-delete.html')


