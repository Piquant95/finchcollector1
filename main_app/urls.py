from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_updates/', views.add_updates, name='add_updates'),
    path('upgrade/', views.UpgradeList.as_view(), name='upgrade_index'),
    path('upgrade/<int:pk>/', views.UpgradeDetail.as_view(), name='upgrade_detail'),
    path('upgrade/create/', views.UpgradeCreate.as_view(), name='upgrade_create'),
    path('upgrade/<int:pk>/update/', views.UpgradeUpdate.as_view(), name='upgrade_update'),
    path('upgrade/<int:pk>/delete/', views.UpgradeDelete.as_view(), name='upgrade_delete'),
    path('cars/<int:car_id>/assoc_upgrade/<int:upgrade_id>/', views.assoc_upgrade, name='assoc_upgrade'),
    path('cars/<int:car_id>/delete_upgrade/<int:upgrade_id>/', views.delete_upgrade, name='delete_upgrade'),
]