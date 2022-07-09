from rest_framework import status
from django.urls import reverse
from .test_setup import TestSetUp


class TestAnomaliesApi(TestSetUp):

    def test_count_anomalies_url_hit(self):
        response = self.client.get(reverse('count_anomalies_landing'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anomalies_using_parameterized_sensor(self):
        response = self.client.get(reverse('count_anomalies', kwargs=self.param['input']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
            f"The count of anomalies for sensor_id {self.param['input']['sensor_id']} is {self.param['expected_output']}")



