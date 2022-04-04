import datetime

from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.db import models

'''The user must provide the following information in their profile:
The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:
Date of birth: day, month, and year of birth.
Description - a user can write any description about themselves, no limit of words/chars.
Email - a user can only write a valid email address.
Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
'''
UserModel = get_user_model()


class Pet(models.Model):
    # Constants
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    NAME_MAX_LENGTH = 30

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    data_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property  # За дата на раждане в dashboard.html
    def age(self):
        return datetime.datetime.now().year - self.data_of_birth.year

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = cloudinary_models.CloudinaryField('image')

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
