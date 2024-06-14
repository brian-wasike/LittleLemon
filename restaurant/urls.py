from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'booking', views.BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]