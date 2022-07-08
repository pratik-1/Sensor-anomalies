
# from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from anomalies.helper_functions import get_model_from_sensor_id, get_readings_from_sensor_id, count_anomalies


class CountAnomalies(APIView):
    """
    View for authenticated users to find number of anomalies
    """
    def get(self, request, sensor_id=None, format=None):
        print(sensor_id)
        if sensor_id is None:
            # data = {"sensor_id": sensor_id}
            return Response('Provide the sensor_id in query parmeter: /count-anomalies/cr123/')
        elif sensor_id:
            model = get_model_from_sensor_id(sensor_id)
            readings = get_readings_from_sensor_id(sensor_id)
            count = count_anomalies(readings, model)
            return Response(f'The number of anomalies for sensor_id {sensor_id} is {count}')
