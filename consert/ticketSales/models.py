from django.db import models
from django.shortcuts import reverse
from account.models import CustomUser
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.


class Consert(models.Model):
    name = models.CharField(max_length=50)
    singer_name = models.CharField(max_length=50)
    length = models.IntegerField()
    poster = models.ImageField(
        upload_to="consertPoster/", height_field=None, width_field=None, null=True)

    class Meta:
        verbose_name = "consert"
        verbose_name_plural = "conserts"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("consert_detail", kwargs={"pk": self.pk})


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})


class TimeConsert(models.Model):
    STATUS_CHOICES = (("start", "start"),
                      ("end", "end"),
                      ("cancel", "cancel"),
                      ("sales", "sales"),)
    consert = models.ForeignKey(
        Consert, verbose_name="time consert", on_delete=models.CASCADE, related_name='timeConsert')
    location = models.ForeignKey(
        Location, verbose_name="time location", on_delete=models.CASCADE, related_name='timeLocation')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    seats = models.IntegerField()
    # status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def set_status(self):
        now = timezone.now()
        if now < self.start_time:
            return 'sales'
        elif now > self.start_time and now < (self.start_time + timedelta(minutes=self.consert.length)):
            return 'start'

        else:
            return 'cancel or end !!!!'

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
        ordering = ("-start_time",)

    def __str__(self):
        return f'{self.consert.name} {self.location.name} {self.start_time}'

    def get_absolute_url(self):
        return reverse("Time_detail", kwargs={"pk": self.pk})


class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time = models.ForeignKey(TimeConsert, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="ticketImages/", height_field=None, width_field=None, null=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"user info:{self.user.full_name} consert info:{self.time.consert.name},{self.time.location}"

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"pk": self.pk})


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=(
        "user"), on_delete=models.CASCADE, related_name="Favorites")
    consert = models.ForeignKey(Consert, verbose_name=(
        "consert"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Favorite")
        verbose_name_plural = ("Favorites")

    def __str__(self):
        return self.consert.name

    def get_absolute_url(self):
        return reverse("Favorite_detail", kwargs={"pk": self.pk})
