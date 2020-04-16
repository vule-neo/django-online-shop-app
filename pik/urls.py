from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "pik"

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("post-view/<int:pk>/", PostDetailView.as_view(), name="post-view"),
	path("create-post", CreatePostView.as_view(), name="create-post"),
	path("/<str:cat>/-posts/", category_view, name="category-view"),
	path("delete-post/<int:pk>/", PostDeleteView.as_view(), name="delete-post"),
	path("user-profile/<int:id>/", user_profile, name="user-profile"),
	path("posts-search/", search, name="posts-search"),
	path("posts-questions/<int:id>/", questions, name="post-questions"),
	path("delete-question/<int:id>/", delete_question, name="delete-question"),
	path("determine-price/", determine_price, name="determine-price"),
	path("update-post/<int:pk>/", PostUpdateView.as_view(), name="update-post"),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
