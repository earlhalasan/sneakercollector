from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_release/', views.add_release, name='add_release'),
    path('purposes/', views.PurposeList.as_view(), name='purposes_index'),
    path('purposes/<int:pk>/', views.PurposeDetail.as_view(), name='purposes_detail'),
    path('purposes/create/', views.PurposeCreate.as_view(), name='purposes_create'),
    path('purposes/<int:pk>/update/', views.PurposeUpdate.as_view(), name='purposes_update'),
    path('purposes/<int:pk>/delete/', views.PurposeDelete.as_view(), name='purposes_delete'),
    path('sneakers/<int:sneaker_id>/assoc_purpose/<int:purpose_id>/', views.assoc_purpose, name='assoc_purpose'),
]