from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import create_blog

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('pages/<int:blog_id>/', views.page_detail, name='page_detail'),
    path('create/', create_blog, name='create_blog'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('pages/<int:blog_id>/', views.page_detail, name='blog_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)