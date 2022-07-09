import os
from os.path import exists
from anomalies.helper_functions import get_data_from_sensor_id, get_count_anomalies, count_anomalies


def test_get_data_from_sensor_id():
    data_file = exists(os.path.join('anomalies/static', 'data.json'))
    model_file = exists(os.path.join('anomalies/static', 'model.json'))
    model_incorrect_path = exists('model.json')

    model = get_data_from_sensor_id(filename='model.json', sensor_id='cr123')
    data = get_data_from_sensor_id(filename='data.json', sensor_id='cr123')
    model_file_notfound = get_data_from_sensor_id(filename='mo.json', sensor_id='cr123')

    assert data_file == True
    assert model_file == True
    assert model_incorrect_path == False
    assert model_file_notfound is None

    assert isinstance(model, list)
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_count_anomalies():
    count = get_count_anomalies('cr123')
    assert count == 8


def test_count_anomalies():
    model = get_data_from_sensor_id(filename='model.json', sensor_id='cr123')
    model = model[0]
    readings = get_data_from_sensor_id(filename='data.json', sensor_id='cr123')

    nsigma = model['n_sigma']
    sigma = model['sigma']

    assert nsigma is not None
    assert sigma is not None
    assert len(model['means']) == len(readings[0]['samples'])

    count = count_anomalies(readings, model)
    assert isinstance(count, int)
