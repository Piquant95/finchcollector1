from django.db import models
from django.urls import reverse
from datetime import date



SERVICE = (
    ('O', 'Oil change'),
    ('T', 'Tire change'),
    ('C', 'Check up')
)

# Create your models here.


class Upgrade(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('upgrade_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    upgrade = models.ManyToManyField(Upgrade)

    def __str__(self):
        return f'{self.make} ({self.id})'
    
    def get_absolute_url(self):
        return reverse ('detail', kwargs={'car_id' : self.id})
    
    def updates_for_today(self):
        return self.updates_set.filter(date=date.today()).count() >= len(SERVICE)
    


class Updates(models.Model):
    date = models.DateField('service date')
    service = models.CharField(max_length=1, choices=SERVICE, default=SERVICE[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    

    class Meta:
        ordering = ['-date']

