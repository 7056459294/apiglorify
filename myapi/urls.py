
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'gusers', views.guserViewSet)
router.register(r'hotel', views.hotelViewSet)
router.register(r'users', views.userViewSet)
router.register(r'venue', views.venueViewSet)
router.register(r'vendor', views.vendorViewSet)
#router.register(r'users2/<str:pk>', views.userViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
   
]