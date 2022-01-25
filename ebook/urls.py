from django.urls import path, include
from .views import Create_ebook, Update_ebook

urlpatterns = [
    path('create/', Create_ebook.as_view(),name="get_post_ebook"),
    path('create/<int:pk>', Update_ebook.as_view(),name="get_update_del_ebook"),


]
