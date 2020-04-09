from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from schedule.api.serializers import ServiceSerializer, ClientSerializer, \
        ProfessionalSerializer, AppointmentSerializer
from schedule.api.mixins import NotPatchMixin
import datetime


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
    queryset = Appointment.objects.all().order_by('-date', 'start_time', 'finish_time')
    serializer_class = AppointmentSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        try:
            return super(AppointmentViewSet, self).list(*args, **kwargs)
        except ValueError as verror:
            return Response({ 'error': str(verror) }, status=400)

    def get_queryset(self):
        qs = self.queryset

        query_state = self.request.query_params.get('state')
        if query_state:
            if query_state not in ('S', 'Y', 'N'):
                raise ValueError('state must be S, Y or N')
            qs = qs.filter(state=query_state)

        query_date_str = self.request.query_params.get('date')
        if query_date_str:
            query_date = datetime.datetime.strptime(query_date_str, '%Y-%m-%d').date()
            qs = qs.filter(date=query_date)

        query_client_id = self.request.query_params.get('clientId')
        if query_client_id:
            qs = qs.filter(client__id=query_client_id)

        query_professional_id = self.request.query_params.get('professionalId')
        if query_professional_id:
            qs = qs.filter(professional__id=query_professional_id)

        query_service_id = self.request.query_params.get('serviceId')
        if query_service_id:
            qs = qs.filter(service__id=query_service_id)

        return qs
