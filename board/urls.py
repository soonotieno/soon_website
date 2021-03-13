"""my_site_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('free_board/', views.BoardList.as_view()),
    path('free_board/<int:pk>/', views.BoardDetail.as_view()),
    path('create/free_board/', views.BoardCreate.as_view()),
    path('update_board/<int:pk>/', views.BoardUpdate.as_view()),
    path('free_board/<int:pk>/new_comment/', views.new_comment),
    path('free_board/update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('free_board/delete_comment/<int:pk>/', views.delete_comment),

    # path('search/<str:q>/', views.PostSearch.as_view()),
    # path('tag/<str:slug>/', views.PostListByTag.as_view()),
    # path('category/<str:slug>/', views.PostListByCategory.as_view()),
    # # path('delete_comment/<int:pk>/', views.CommentDelete.as_view()), #CBV(Class Base View)에 입각한 댓글 삭제 구현 url 코드
    # path('edit_comment/<int:pk>/', views.CommentUpdate.as_view()),
    # path('delete_comment/<int:pk>/', views.delete_comment),
    # path('<int:pk>/new_comment/', views.new_comment),
    # path('<int:pk>/update/', views.PostUpdate.as_view()),
    # path('<int:pk>/', views.PostDetail.as_view()),
    # path('create/', views.PostCreate.as_view()),
    # path('', views.PostList.as_view()),
]
