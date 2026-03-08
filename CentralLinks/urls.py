from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("links/create/", views.create_link, name="create"),
    path("links/search/", views.search_links, name="search_links"),
    path("links/<int:link_id>/update/", views.modify_link ),
    path("links/<int:link_id>/delete/", views.delete_link, name="delete"),
]