from django.db import models
from django.core.exceptions import ValidationError


class Channel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    bidtypes = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.bidtypes = self.bidtypes.replace(', ', ',')
        super().save()


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    bid = models.FloatField()
    bidtype = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        channel_bidtypes = self.channel.bidtypes.split(',')
        if self.bidtype not in channel_bidtypes:
            raise ValidationError("Capmaign's BidType '%s' not in Channel's Bidtypes" % self.bidtype)
        super().save()
