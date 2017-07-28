
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from ad.models import Channel, Campaign

# Create your views here.

# Channel CBV


class ChannelList(ListView):
    model = Channel


class ChannelCreate(CreateView):
    model = Channel
    success_url = reverse_lazy('ad:channel_list')
    fields = ['name', 'slug', 'bidtypes']


class ChannelUpdate(UpdateView):
    model = Channel
    success_url = reverse_lazy('ad:channel_list')
    fields = ['name', 'slug', 'bidtypes']


class ChannelDelete(DeleteView):
    model = Channel
    success_url = reverse_lazy('ad:channel_list')


# Campaign CBV


class CampaignList(ListView):
    model = Campaign


class CampaignCreate(CreateView):
    model = Campaign
    success_url = reverse_lazy('ad:campaign_list')
    fields = ['name', 'channel', 'bid', 'bidtype']


class CampaignUpdate(UpdateView):
    model = Campaign
    success_url = reverse_lazy('ad:campaign_list')
    fields = ['name', 'channel', 'bid', 'bidtype']


class CampaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('ad:campaign_list')