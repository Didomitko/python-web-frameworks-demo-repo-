from django.views.generic import TemplateView, ListView

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto


class HomeView(RedirectToDashboard, TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'

# def show_dashboard(request):
#     profile = get_profile()
#     # if not profile:
#     #     return redirect('401')
#     pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'main/dashboard.html', context)
