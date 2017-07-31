from django.test import TestCase, Client
from ad.models import Channel, Campaign
from django.core.urlresolvers import reverse


class ChannelViewTests(TestCase):
    def setUp(self):
        Channel.objects.create(name='test_name1',
                               slug='test_slug1',
                               bidtypes='a,bc, d, ef')
        Channel.objects.create(name='test_name2',
                               slug='test_slug2',
                               bidtypes='abc, def')
        self.client = Client()

    def test_create_channel(self):
        url = reverse('ad:channel_create')
        data = {'name': 'test_name3',
                'slug': 'test_slug3',
                'bidtypes': 'ab, cd'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Channel.objects.count(), 3)
        self.assertEqual(Channel.objects.get(name='test_name3').slug, 'test_slug3')

    def test_view_channels_list(self):
        url = reverse('ad:channel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_update_channel(self):
        channel = Channel.objects.get(name='test_name1')
        url = reverse('ad:channel_update', args=[channel.id])
        data = {"name": "test_name3",
                "slug": "test_slug3",
                "bidtypes": "ab, cd"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Channel.objects.count(), 2)
        self.assertEqual(Channel.objects.get(name='test_name3').slug, 'test_slug3')

    def test_delete_channel(self):
        channel = Channel.objects.get(name='test_name1')
        url = reverse('ad:channel_delete', args=[channel.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Channel.objects.get().name, 'test_name2')


class CampaignViewTests(TestCase):
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
        self.client = Client()

    def test_create_campaign(self):
        url = reverse('ad:campaign_create')
        data = {'name': 'test_name4',
                'channel': Channel.objects.get().id,
                'bid': 1.1,
                'bidtype': 'bc'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Campaign.objects.count(), 3)
        self.assertEqual(Campaign.objects.get(name='test_name4').bidtype, 'bc')

    def test_view_campaign_list(self):
        url = reverse('ad:campaign_list')
        response = self.client.get(url)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_update_campaign(self):
        campaign = Campaign.objects.get(name='test_name2')
        url = reverse('ad:campaign_update', args=[campaign.id])
        data = {'name': 'test_name4',
                'channel': Channel.objects.get().id,
                'bid': 99.2,
                'bidtype': 'bc'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Campaign.objects.get(name='test_name4').bid, 99.2)

        # # wrong bidtype
        # data = {'name': 'test_name5',
        #         'channel': Channel.objects.get().id,
        #         'bid': 99.2,
        #         'bidtype': 'asdasd'}
        # response = self.client.post(url, data)
        # self.assertEqual(response.status_code, 400)

    def test_delete_campaign(self):
        campaign = Campaign.objects.get(name='test_name2')
        url = reverse('ad:campaign_delete', args=[campaign.id])
        response = self.client.delete(url)
        self.assertEqual(Campaign.objects.get().name, 'test_name3')
        self.assertEqual(Campaign.objects.count(), 1)





class CampaginViewTests(TestCase):
    pass


'''
class Channel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    bidtypes = models.CharField(max_length=100)


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    bid = models.FloatField()
    bidtype = models.CharField(max_length=100)
'''