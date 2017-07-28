from django.conf.urls import url
from ad import views

app_name = 'ad'

urlpatterns = [
    url(r'^channels/$', views.ChannelList.as_view(), name='channel_list'),
    url(r'^channels/create/$', views.ChannelCreate.as_view(), name='channel_create'),
    url(r'^channels/update/(?P<pk>\d+)/$', views.ChannelUpdate.as_view(), name='channel_update'),
    url(r'^channels/delete/(?P<pk>\d+)/$', views.ChannelDelete.as_view(), name='channel_delete'),
    url(r'^campaigns/$', views.CampaignList.as_view(), name='campaign_list'),
    url(r'^campaigns/create/$', views.CampaignCreate.as_view(), name='campaign_create'),
    url(r'^campaigns/update/(?P<pk>\d+)/$', views.CampaignUpdate.as_view(), name='campaign_update'),
    url(r'^campaigns/delete/(?P<pk>\d+)/$', views.CampaignDelete.as_view(), name='campaign_delete'),
]