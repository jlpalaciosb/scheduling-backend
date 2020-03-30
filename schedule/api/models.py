from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    professionals = models.ManyToManyField('api.Professional', blank=True)


class Person(models.Model):
    document = models.CharField(max_length=50,
            help_text='e.g.: The person\'s ID number', unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=101)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        return super(Person, self).save(*args, **kwargs)


class Client(Person):
    pass


class Professional(Person):
    services = models.ManyToManyField(Service, blank=True)
    pass


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    state = models.CharField(max_length=1, choices=(('S', 'Scheduled'),
            ('Y', 'Did attend'), ('N', 'Did not attend')))
    comment = models.CharField(max_length=300, blank=True)
