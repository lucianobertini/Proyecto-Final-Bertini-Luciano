from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/list/', views.profile_list, name='profile_list'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'), 
    path('user-profile/', views.user_profile, name='user_profile'),
]
