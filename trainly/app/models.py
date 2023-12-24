from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']
    def __str__(self):
        return self.username


class Train(models.Model):
    number=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)

class TrainStops(models.Model):
    number=models.ForeignKey(Train,on_delete=models.CASCADE)
    stop=models.TextField(max_length=50)
    arrival=models.TimeField()
    departure=models.TimeField()
    def __str__(self):
        return str(self.number)+' '+self.stop

class TrainSeats(models.Model):
    number=models.ForeignKey(Train,on_delete=models.CASCADE)
    class_type=models.TextField(max_length=2)
    total=models.IntegerField()
    available=models.IntegerField()
    def __str__(self):
        return str(self.number)+' '+self.class_type

class UserJourneys(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    PNR=models.IntegerField(primary_key=True)
    start_stop=models.TextField()
    end_stop=models.TextField()
    def __str__(self):
        return str(self.PNR)

class JourneyPassengers(models.Model):
    PNR=models.ForeignKey(UserJourneys,on_delete=models.CASCADE)
    class_type=models.TextField(max_length=2)
    name=models.TextField(max_length=50)
    age=models.IntegerField()
    def __str__(self):
        return str(self.PNR)+' '+self.name
