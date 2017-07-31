from rest_framework import serializers
from ad.models import Channel, Campaign
from django.shortcuts import get_object_or_404


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'slug', 'bidtypes')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'channel', 'bid', 'bidtype')

    def validate_bidtype(self, value):
        """
        Check that the campaign's bidtype is in channel's bidtypes
        """
        channel_id = self.initial_data['channel']
        channel = get_object_or_404(Channel, pk=channel_id)
        available_bidtypes = channel.bidtypes.split(',')
        if value not in available_bidtypes:
            raise serializers.ValidationError("that bidtype is not available in chosen channel")
        return value
