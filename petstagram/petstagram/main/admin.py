

from django.contrib import admin

from petstagram.main.models import Pet, PetPhoto


class PetInLineAdmin(admin.StackedInline):    #прави форми за създаване в профила
    model = Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
