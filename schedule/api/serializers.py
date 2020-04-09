from schedule.api.models import Service, Client, Professional, Appointment
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'category', 'url']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'document', 'first_name', 'last_name',
                  'email_address', 'phone_number', 'date_of_birth', 'url']


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'document', 'first_name', 'last_name', 'email_address',
                  'phone_number', 'date_of_birth', 'services', 'url']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    service_name = serializers.SerializerMethodField()
    client_short_full_name = serializers.SerializerMethodField()
    professional_short_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'start_time', 'finish_time', 'client',
                  'professional', 'service', 'state', 'comment', 'url',
                  'service_name', 'client_short_full_name', 'professional_short_full_name']
        read_only_fields = ['service_name', 'client_short_full_name',
                            'professional_short_full_name']

    def validate(self, data):
        if not data['start_time'] < data['finish_time']:
            raise serializers.ValidationError({'finishTime': 'finish time must occur after start time'})

        aid = -1 # Updating appointment id, -1 if new appointment (POST)
        if self.instance is not None: aid = self.instance.id
        if data['professional'].appointment_set.exclude(id=aid).filter(state='S', date=data['date'],
                finish_time__gt=data['start_time'], start_time__lt=data['finish_time']).count() > 0:
            raise serializers.ValidationError({'professional': 'busy in the given time slot'})

        return data

    def get_service_name(self, appointment):
        return appointment.service.name

    def get_client_short_full_name(self, appointment):
        return appointment.client.first_name.split()[0] + ' ' + \
               appointment.client.last_name.split()[0]

    def get_professional_short_full_name(self, appointment):
        return appointment.professional.first_name.split()[0] + ' ' + \
               appointment.professional.last_name.split()[0]
