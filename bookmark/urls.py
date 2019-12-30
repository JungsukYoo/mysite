from django.urls import path
from bookmark.views import BookmarkDV, BookmarkLV


app_name = 'bookmark'
urlpatterns = [
    # Class-based views
    path('', BookmarkLV.as_view(), name='idex'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
