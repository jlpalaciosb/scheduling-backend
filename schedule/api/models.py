from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    professionals = models.ManyToManyField('api.Professional')


class Person(models.Model):
    id_document = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Client(Person):
    pass


class Professional(Person):
    services = models.ManyToManyField(Service)
    pass


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    state = models.CharField(max_length=1, choices=(('S', 'Scheduled'),
            ('Y', 'Did attend'), ('N', 'Did not attend')))
    comment = models.CharField(max_length=300, blank=True)
