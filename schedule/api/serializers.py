from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'url', 'name', 'description', 'category']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'url', 'document', 'first_name', 'last_name',
                  'email_address', 'phone_number', 'date_of_birth']


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'url', 'document', 'first_name', 'last_name', 'email_address',
                  'phone_number', 'date_of_birth', 'services']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    client_name = serializers.SerializerMethodField()
    professional_name = serializers.SerializerMethodField()
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'url', 'date', 'start_time', 'finish_time', 'client', 'client_name',
                  'professional', 'professional_name', 'service', 'service_name',
                  'state', 'comment']
        read_only_fields = ['client_name', 'professional_name', 'service_name']

    def validate(self, data):
        if not data['start_time'] < data['finish_time']:
            raise serializers.ValidationError({'finishTime': 'finish time must occur after start time'})

        aid = -1 # Updating appointment id, -1 if new appointment (POST)
        if self.instance is not None: aid = self.instance.id
        if data['professional'].appointment_set.exclude(id=aid).filter(state='S', date=data['date'],
                finish_time__gt=data['start_time'], start_time__lt=data['finish_time']).count() > 0:
            raise serializers.ValidationError({'professional': 'busy in the given time slot'})

        return data

    @staticmethod
    def get_client_name(appointment):
        return '%s %s' % (appointment.client.first_name.split()[0],
                appointment.client.last_name.split()[0])

    @staticmethod
    def get_professional_name(appointment):
        return '%s %s' % (appointment.professional.first_name.split()[0],
                appointment.professional.last_name.split()[0])

    @staticmethod
    def get_service_name(appointment):
        return appointment.service.name
