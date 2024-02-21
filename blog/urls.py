from django.urls import path
from .views import home_view, category_view, blog_single_view, about_view, contact_view

urlpatterns = [
    path('', home_view),
    path('category/', category_view),
    path('blog-single/<int:pk>/', blog_single_view),
    path('about/', about_view),
    path('contact/', contact_view)


]