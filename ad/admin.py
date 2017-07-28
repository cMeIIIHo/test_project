from django.contrib import admin
from ad.models import Channel, Campaign
from django.contrib import admin

# Register your models here.


class CampaignInline(admin.StackedInline):
    model = Campaign


class ChannelAdmin(admin.ModelAdmin):
    inlines = [CampaignInline]


admin.site.register(Channel, ChannelAdmin)
