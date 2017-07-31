from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ad_api import views

app_name = 'ad_api'

urlpatterns = [
    url(r'^channels/$', views.ChannelListApi.as_view()),
    url(r'^channels/(?P<pk>[0-9]+)/$', views.ChannelDetailApi.as_view()),
    url(r'^campaigns/$', views.CampaignListApi.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.CampaignDetailApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)