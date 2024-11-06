from django.urls import path
from .views import ItemList

urlpatterns = [
    path('items/', ItemList.as_view(), name='itemlist')
]



# # myapp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('items/', views.ItemList.as_view(), name='item-list'),
#     path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
# ]
