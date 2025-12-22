from django.urls import path, include
from django.contrib.auth import views as auth_views

from blog import views

app_name = 'blog'


post_patterns = [
    path(
        '<int:post_id>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        '<int:post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(
        '<int:post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),
    path(
        '<int:post_id>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        '<int:post_id>/comments/<int:comment_id>/edit/',
        views.CommentUpdateView.as_view(),
        name='edit_comment'
    ),
    path(
        '<int:post_id>/comments/<int:comment_id>/delete/',
        views.CommentDeleteView.as_view(),
        name='delete_comment'
    ),
]


urlpatterns = [
    # Главная
    path('', views.PostListView.as_view(), name='index'),

    # Посты
    path('posts/', include((post_patterns, app_name))),

    # Категории
    path(
        'category/<slug:category_slug>/',
        views.CategoryPostListView.as_view(),
        name='category_posts'
    ),

    # Профиль
    path(
        'profile/edit/',
        views.EditProfileView.as_view(),
        name='edit_profile'
    ),
    path(
        'profile/<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),

    # Создание поста
    path(
        'create/',
        views.PostCreateView.as_view(),
        name='create_post'
    ),

    # Смена пароля
    path(
        'profile/password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html',
            success_url='/'
        ),
        name='password_change'
    ),
]
