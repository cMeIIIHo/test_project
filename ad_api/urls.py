from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ad_api import views

app_name = 'ad_api'

urlpatterns = [
    url(r'^channels/$', views.ChannelListApi.as_view(), name='channel_list_api'),
    url(r'^channels/(?P<pk>[0-9]+)/$', views.ChannelDetailApi.as_view(), name='channel_detail_api'),
    url(r'^campaigns/$', views.CampaignListApi.as_view(), name='campaign_list_api'),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.CampaignDetailApi.as_view(), name='campaign_detail_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)