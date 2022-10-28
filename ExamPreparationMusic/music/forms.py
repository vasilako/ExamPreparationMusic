from django import forms

from ExamPreparationMusic.music.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class AlbumAddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'URL image'}),
            'description': forms.Textarea(attrs={'placeholder': 'OPTIONAL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Wite down the price'}),
        }


class AlbumEditForm(forms.ModelForm):
    class Meta():
        model = Album
        fields = '__all__'

class AlbumDeleteForm(forms.ModelForm):
    class Meta():
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'readonly': True}),
            'artist': forms.TextInput(attrs={'readonly': True}),
            'genre': forms.URLInput(attrs={'readonly': True}),
            'image_url': forms.URLInput(attrs={'readonly': True}),
            'description': forms.Textarea(attrs={'readonly': True}),
            'price': forms.NumberInput(attrs={'readonly': True}),
        }
    def save(self, commit=True):
        if commit == True:
            self.instance.delete()

        return self.instance










