from django.urls import path
from .views import *

app_name = "day_code"

urlpatterns = [
    path('', CodeBlockListView.as_view(), name='block_list'),
    path('block/create/', CodeBlockCreateView.as_view(), name='block_create'),
    path('block/<pk>/', CodeBlockDetailView.as_view(), name='block_detail'),
    path('block/<pk>/edit/', CodeBlockUpdateView.as_view(), name='block_edit'),
    path('block/<pk>/delete/', CodeBlockDeleteView.as_view(), name='block_delete'),
    path("block/<pk>/add_page/", add_page_to_block, name="add_page_to_block"),
    path("page/<pk>/detail", page_detail, name="page_detail"),
    path("page/<pk>/remove", remove_page, name="page_remove")
]
