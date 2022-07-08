import json
from pprint import pprint


def get_model_from_sensor_id(sensor_id):
    with open('anomalies/static/model.json') as data_file:
        data = json.load(data_file)
    # pprint(data)
    for d in data:
        # print(d)
        if d['sensor_id'] == sensor_id:
            print('\n ****************Model')
            pprint(d)
            return d
    return None


def get_readings_from_sensor_id(sensor_id):
    with open('anomalies/static/data.json') as data_file:
        data = json.load(data_file)
    print('\n ****************Data')
    s_readings = []
    for d in data:
        if d['sensor_id'] == sensor_id:
            # pprint(d)
            s_readings.append(d)
    pprint(s_readings)
    return s_readings


def get_count_anomalies(sensor_id):
    model = get_model_from_sensor_id(sensor_id)
    readings = get_readings_from_sensor_id(sensor_id)
    count = count_anomalies(readings, model)
    return count


def count_anomalies(readings, model):
    nsigma = model['n_sigma']
    sigma = model['sigma']
    count = 0
    means_i = model['means']
    # pprint(reading['samples'])
    for reading in readings:
        for ix, sample_i in enumerate(reading['samples']):
            if abs(sample_i - means_i[ix]) > nsigma * sigma:
                count += 1
    print(count)
    return count






