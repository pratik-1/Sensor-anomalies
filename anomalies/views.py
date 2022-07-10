from rest_framework.views import APIView
from rest_framework.response import Response

from anomalies.helper_functions import get_count_anomalies


class CountAnomalies(APIView):
    """
    View for authenticated users to find count of anomalies
    """
    def get(self, request, sensor_id=None, format=None):
        if sensor_id is None:
            return Response({'message': 'Please provide the SensorId in query parameter (For ex: /count-anomalies/cr123/)'}, status=200)
        elif sensor_id:
            try:
                count = get_count_anomalies(sensor_id)
            except:
                return Response({'message': f'Sorry sensor_id not found in model database. Please try different ID.'}, status=204)
            else:
                return Response({'message': f'The count of anomalies for sensor_id {sensor_id} is {count}'}, status=200)