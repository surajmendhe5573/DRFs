from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='itemlist'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='itemdetail')
]
