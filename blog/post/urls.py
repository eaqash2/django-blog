from django.urls import path

from post import views

app_name = "post"

urlpatterns = [
    path(
        "all/",
        views.PostListView.as_view(),
        name="post_list",
    ),
    path(
        "<int:pk>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
]