from django.urls import path

from members.views import UserRegisterView, UserEdit
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit-profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
]