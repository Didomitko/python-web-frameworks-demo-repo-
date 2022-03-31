from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.helps import BootstrapFormMixin, DisabledFieldsFormMixin
from petstagram.main.models import Pet


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'data_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE = date(1920, 1, 1)
    MAX_DATE = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_data_of_birth(self):
        data_of_birth = self.cleaned_data['data_of_birth']
        if data_of_birth < self.MIN_DATE or self.MAX_DATE < data_of_birth:
            raise ValidationError(f'Date of birth must be between {self.MIN_DATE} and {self.MAX_DATE}')
        return data_of_birth

    class Meta:
        model = Pet
        exclude = ('user_profile',)
        widgets = {
                'data_of_birth': forms.DateInput,
            }


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    # ako искаме нещо да е отключено тук слагаме disabled_fields = ('това което искаме да заключим')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
