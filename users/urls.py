from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserPasswordChangeView, UserUpdateView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('user/edit_profile/', UserUpdateView.as_view(), name='edit_profile'),
]
