from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CheckConstraint, Q, F

# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'Users'
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    wallet = models.FloatField(default=0)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']
    def __str__(self):
        return self.username


class Train(models.Model):
    class Meta:
        verbose_name_plural = 'Trains'
    number=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)

class TrainStops(models.Model):
    class Meta:
        verbose_name_plural = 'TrainStops'
    number=models.ForeignKey(Train,on_delete=models.CASCADE)
    stop=models.TextField(max_length=50)
    arrival=models.TimeField()
    departure=models.TimeField()
    def __str__(self):
        return self.stop

class TrainSeats(models.Model):
    class Meta:
        verbose_name_plural = 'TrainSeats'
    number=models.ForeignKey(Train,on_delete=models.CASCADE)
    class_type=models.TextField(max_length=2)
    total=models.IntegerField()
    available=models.IntegerField()
    fare=models.PositiveIntegerField()
    def __str__(self):
        return str(self.number)+' '+self.class_type

class UserJourneys(models.Model):
    class Meta:
        verbose_name_plural = 'UserJourneys'
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number=models.ForeignKey(Train,on_delete=models.CASCADE)
    PNR=models.IntegerField(primary_key=True)
    start_stop=models.ForeignKey(TrainStops,related_name="start_stop",on_delete=models.CASCADE)
    end_stop=models.ForeignKey(TrainStops,related_name="end_stop",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.PNR)

class JourneyPassengers(models.Model):
    class Meta:
        verbose_name_plural = 'JourneyPassengers'
    PNR=models.ForeignKey(UserJourneys,on_delete=models.CASCADE)
    class_type=models.ForeignKey(TrainSeats,on_delete=models.CASCADE)
    name=models.TextField(max_length=50)
    age=models.IntegerField()
    def __str__(self):
        return str(self.PNR)+' '+self.name
