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


class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'document', 'first_name', 'last_name', 'email_address',
                  'phone_number', 'date_of_birth', 'services']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'date', 'start_time', 'finish_time', 'client',
                  'professional', 'service', 'state', 'comment']

    def validate(self, data):
        if not data['start_time'] < data['finish_time']:
            raise serializers.ValidationError({
                'finishTime': 'finish time must occur after start time'})
        return data
