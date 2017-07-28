from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ad_api import views

app_name = 'ad_api'

urlpatterns = [
    url(r'^channels/$', views.ChannelList.as_view()),
    url(r'^channels/(?P<pk>[0-9]+)/$', views.ChannelDetail.as_view()),
    url(r'^campaigns/$', views.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.CampaignDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)