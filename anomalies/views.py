from rest_framework.views import APIView
from rest_framework.response import Response

from anomalies.helper_functions import get_count_anomalies


class CountAnomalies(APIView):
    """
    View for authenticated users to find number of anomalies
    """
    def get(self, request, sensor_id=None, format=None):
        print(sensor_id)
        if sensor_id is None:
            return Response('Provide the sensor_id in query parmeter (For ex: /count-anomalies/cr123/)')
        elif sensor_id:
            count = get_count_anomalies(sensor_id)
            return Response(f'The count of anomalies for sensor_id {sensor_id} is {count}')
