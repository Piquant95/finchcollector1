from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('states/', views.states_index, name='index'),
    path('states/<int:state_id>/', views.states_detail, name='detail'),
    path('states/create/', views.StateCreate.as_view(), name='states_create'),
    path('states/<int:pk>/update/', views.StateUpdate.as_view(), name='states_update'),
    path('states/<int:pk>/delete/', views.StateDelete.as_view(), name='states_delete'),
    path('states/<int:state_id>/add_updates/', views.add_updates, name='add_updates'),
    path('upgrade/', views.UpgradeList.as_view(), name='upgrade_index'),
    path('upgrade/<int:pk>/', views.UpgradeDetail.as_view(), name='upgrade_detail'),
    path('upgrade/create/', views.UpgradeCreate.as_view(), name='upgrade_create'),
    path('upgrade/<int:pk>/update/', views.UpgradeUpdate.as_view(), name='upgrade_update'),
    path('upgrade/<int:pk>/delete/', views.UpgradeDelete.as_view(), name='upgrade_delete'),
    path('states/<int:state_id>/assoc_upgrade/<int:upgrade_id>/', views.assoc_upgrade, name='assoc_upgrade'),
    path('states/<int:state_id>/delete_upgrade/<int:upgrade_id>/', views.delete_upgrade, name='delete_upgrade'),
]