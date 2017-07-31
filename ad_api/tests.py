from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ad.models import Channel, Campaign

# create, read, update, delete


class ChannelApiTests(APITestCase):
    def setUp(self):
        Channel.objects.create(name='test_name1',
                               slug='test_slug1',
                               bidtypes='a,bc, d, ef')
        Channel.objects.create(name='test_name2',
                               slug='test_slug2',
                               bidtypes='abc, def')

    def test_create_channel(self):
        url = reverse('ad_api:channel_list_api')
        data = {'name': 'test_name3',
                'slug': 'test_slug3',
                'bidtypes': 'ab,c, df, g'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Channel.objects.count(), 3)
        self.assertEqual(Channel.objects.get(name='test_name3').slug, 'test_slug3')

    def test_get_channel(self):
        channel = Channel.objects.get(name='test_name1')
        url = reverse('ad_api:channel_detail_api', args=[channel.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], 'test_slug1')

    def test_update_channel(self):
        channel = Channel.objects.get(name='test_name1')
        url = reverse('ad_api:channel_detail_api', args=[channel.id])
        data = {'name': 'test_name3',
                'slug': 'test_slug3',
                'bidtypes': 'ab,c, df, g'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], 'test_slug3')

    def test_delete_channel(self):
        channel = Channel.objects.get(name='test_name1')
        url = reverse('ad_api:channel_detail_api', args=[channel.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Channel.objects.count(), 1)


class CampaignApiTests(APITestCase):
    def setUp(self):
        channel = Channel.objects.create(name='test_name1',
                               slug='test_slug1',
                               bidtypes='a,bc, d, ef')
        Campaign.objects.create(name='test_name2',
                                channel=channel,
                                bid=3.14,
                                bidtype='a')
        Campaign.objects.create(name='test_name3',
                                channel=channel,
                                bid=999.99,
                                bidtype='ef')

    def test_create_campaign(self):
        url = reverse('ad_api:campaign_list_api')
        data = {'name': 'test_name4',
                'channel': Channel.objects.get().id,
                'bid': '2.2',
                'bidtype': 'd'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Campaign.objects.count(), 3)
        self.assertEqual(Campaign.objects.get(name='test_name4').bid, 2.2)

    def test_get_campaign(self):
        campaign = Campaign.objects.get(name='test_name2')
        url = reverse('ad_api:campaign_detail_api', args=[campaign.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bidtype'], 'a')

    def test_update_campaign(self):
        campaign = Campaign.objects.get(name='test_name2')
        url = reverse('ad_api:campaign_detail_api', args=[campaign.id])
        data = {'name': 'test_name4',
                'channel': Channel.objects.get().id,
                'bid': '2.2',
                'bidtype': 'd'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bidtype'], 'd')

    def test_delete_campaign(self):
        campaign = Campaign.objects.get(name='test_name2')
        url = reverse('ad_api:campaign_detail_api', args=[campaign.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Campaign.objects.count(), 1)

    def test_create_wrong_campaign(self):
        url = reverse('ad_api:campaign_list_api')
        data = {'name': 'test_name4',
                'channel': Channel.objects.get().id,
                'bid': '2.2',
                'bidtype': 'asdasd'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Campaign.objects.count(), 2)
