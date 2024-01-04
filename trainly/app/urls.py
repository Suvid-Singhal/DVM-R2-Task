from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home,name='home'),
    path("login/", views.user_login,name='user_login'),
    path("logout/", views.user_logout,name='user_logout'),
    path("search_trains/", views.search_trains,name='search_trains'),
    path("book_tickets/", views.book_tickets,name='book_tickets'),
]