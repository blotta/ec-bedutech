from django.urls import path
from . import views


urlpatterns = [
    path('', views.listing, name='listing'),
    path('<uuid:rma_code>/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('<uuid:rma_code>/edit/', views.edit, name='edit'),
]
    
