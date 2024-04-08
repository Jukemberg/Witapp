from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('account/register/', views.register, name='register'),
    path('account/edit/', views.edit, name='edit'),
]
