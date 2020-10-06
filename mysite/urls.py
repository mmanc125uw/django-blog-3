
from django.contrib import admin
from django.urls import path, include  # <-- Make sure you have both of these imports.

from django.contrib.auth.views import LoginView, LogoutView
from blogging.views import ShortPost_create_view

urlpatterns = [
    path('', include('blogging.urls')),  # <-- add this
    path('polling/', include('polling.urls')),  # <-- Add this
    path('blogging/', include('blogging.urls')),  # <-- Add this
    path('create/', ShortPost_create_view),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('accounts/', include('allauth.urls')),
]
