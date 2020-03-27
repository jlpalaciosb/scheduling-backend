from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from schedule.api import views

router = routers.DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'professionals', views.ProfessionalViewSet)
router.register(r'appointments', views.AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
