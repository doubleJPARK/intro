from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('/<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    # path('<index:pk>/', views.single_post_page),
    # path('', views.index),
]