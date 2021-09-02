from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'gusers', views.guserViewSet)
router.register(r'users', views.userViewSet)
#router.register(r'users2/<str:pk>', views.userViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
   
]