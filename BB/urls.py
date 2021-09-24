from django.urls import path
from .views import PostList, PostDetail, CategoryDetail, SearchResultsListView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentListView, CommentDeleteView, SearchCommentsResultsListView, comment_approved  # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('comment_create/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comments/approved/<int:pk>', comment_approved, name='comment_approved'),
    path('comments/delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('comments/search/', SearchCommentsResultsListView.as_view(), name='search_comments_results'),
]
