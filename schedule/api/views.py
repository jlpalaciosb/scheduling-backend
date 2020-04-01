from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import viewsets, permissions, filters
from schedule.api.serializers import ServiceSerializer, ClientSerializer, \
        ProfessionalSerializer, AppointmentSerializer
from schedule.api.mixins import NotPatchMixin


class ServiceViewSet(NotPatchMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ClientViewSet(NotPatchMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('last_name', 'first_name')
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']


class ProfessionalViewSet(NotPatchMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Professionals to be viewed or edited.
    """
    queryset = Professional.objects.all().order_by('last_name', 'first_name')
    serializer_class = ProfessionalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']


class AppointmentViewSet(NotPatchMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all().order_by('-id')
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
