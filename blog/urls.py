from django.urls import path
from .views import HomePageView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, CommentCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', BlogEditView.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('blog/<int:pk>/comment', CommentCreateView.as_view(), name='comment'),
]
