from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class TestSetUp(APITestCase):
    # this line loads the fixture data with sample users
    fixtures = ["sample.json"]

    def setUp(self):
        super(TestSetUp, self).setUp()
        # this user exists in the fixtures
        user1 = get_user_model().objects.get(username="user1")
        self.client.force_authenticate(user1)
        self.param = {'input': {'sensor_id': 'cr123'}, 'expected_output': 8}
        self.param_wid = {'input': {'sensor_id': 'cr1'}}

    def tearDown(self):
        return super(TestSetUp, self).tearDown()
