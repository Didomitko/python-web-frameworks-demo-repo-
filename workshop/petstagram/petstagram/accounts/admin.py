from django.contrib import admin

from petstagram.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInLineAdmin,)
    list_display = ('first_name', 'last_name')
