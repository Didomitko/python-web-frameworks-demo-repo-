from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from petstagram.accounts.forms import CreateProfileForm
from petstagram.accounts.models import Profile
from petstagram.common.view_mixins import RedirectToDashboard

from petstagram.main.models import Pet, PetPhoto


class UserRegisterView(RedirectToDashboard, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView:
    pass


class ChangeUserPasswordView:
    pass


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_id=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        # .filter(tagged_pets__user_profile=profile).distinct()

        total_likes_count = sum(x.likes for x in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update(
            {
                'total_likes_count': total_likes_count,
                'total_pet_photos_count': total_pet_photos_count,
                'is_owner': self.object.user_id == self.request.user.id,
                'pets': pets,
            }
        )
        return context


# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#     context = {
#         'form': form,
#     }
#     return render(request, template_name, context)
#
#
# def create_profile(request):
#     return profile_action(request, CreateProfileForm, 'index', Profile(), 'main/profile_create.html')
#
#
# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'main/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')

# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CreateProfileForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = EditProfileForm(instance=profile)
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_edit.html', context)





