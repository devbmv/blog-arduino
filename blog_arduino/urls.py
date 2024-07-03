from django.contrib import admin
from django.urls import path
from main_blog_app import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', main_views.debug_view),
]
