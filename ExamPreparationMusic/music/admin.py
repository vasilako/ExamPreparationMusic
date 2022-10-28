from django.contrib import admin

from ExamPreparationMusic.music.models import Profile, Album


# Register your models here.
# En este caso Profile es el modelo

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # el nombre de la clase no importa mucho pero debe herredar admin.ModelAdmin
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin): # el nombre de la clase no importa mucho pero debe herredar admin.ModelAdmin
    pass