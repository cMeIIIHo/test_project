from rest_framework import serializers
from ad.models import Channel, Campaign


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'slug', 'bidtypes')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'channel', 'bid', 'bidtype')