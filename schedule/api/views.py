from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import viewsets, permissions
from schedule.api.serializers import ServiceSerializer, ClientSerializer, \
        ProfessionalSerializer, AppointmentSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('last_name')
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfessionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Professionals to be viewed or edited.
    """
    queryset = Professional.objects.all().order_by('last_name')
    serializer_class = ProfessionalSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all().order_by('-id')
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
