from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/edit/', views.edit_profile_page, name='edit_profile_page'),
    
    # API views
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/profile/', views.UserProfileView.as_view(), name='profile'),
    path('api/profile/picture/', views.ProfilePictureUpdateView.as_view(), name='profile-picture'),
] 