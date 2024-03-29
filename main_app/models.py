from django.db import models
from django.urls import reverse
from datetime import date



CHAMPIONSHIP = (
    ('S', 'Superbowl'),
    ('N', 'NBA Finals'),
    ('W', 'World Series')
)

# Create your models here.


class Upgrade(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('upgrade_detail', kwargs={'pk': self.id})


class State(models.Model):
    name = models.CharField(max_length=100)
    football = models.CharField(max_length=100)
    basketball = models.CharField(max_length=100)
    baseball = models.CharField(max_length=100)
    upgrade = models.ManyToManyField(Upgrade)

    def __str__(self):
        return f'{self.make} ({self.id})'
    
    def get_absolute_url(self):
        return reverse ('detail', kwargs={'state_id' : self.id})
    
    def updates_for_today(self):
        return self.updates_set.filter(date=date.today()).count() >= len(CHAMPIONSHIP)
    


class Updates(models.Model):
    date = models.DateField('Championship date')
    championship = models.CharField(max_length=1, choices=CHAMPIONSHIP, default=CHAMPIONSHIP[0][0])
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_championship_display()} on {self.date}"
    

    class Meta:
        ordering = ['-date']

