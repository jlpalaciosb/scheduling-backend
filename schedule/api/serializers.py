from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'category']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'document', 'first_name', 'last_name',
                  'email_address', 'phone_number', 'date_of_birth']


class ServicesRelatedField(serializers.RelatedField):
    queryset = Service.objects.all()

    def to_representation(self, service):
        return str(service)

    def to_internal_value(self, service_str):
        service_id = service_str.split()[0][3:]
        return self.queryset.get(pk=service_id)


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    services = ServicesRelatedField(many=True)

    class Meta:
        model = Professional
        fields = ['id', 'document', 'first_name', 'last_name', 'email_address',
                  'phone_number', 'date_of_birth', 'services']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'date', 'start_time', 'finish_time', 'client',
                  'professional', 'service', 'state', 'comment']
