from django.urls import path

from petstagram.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),

]