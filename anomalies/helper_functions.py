import json


def get_data_from_sensor_id(filename, sensor_id):
    try:
        with open('anomalies/static/' + filename) as data_file:
            json_data = json.load(data_file)
        data = [d for d in json_data if d['sensor_id'] == sensor_id]
        return data
    except:
        return


def get_count_anomalies(sensor_id):
    model = get_data_from_sensor_id(filename='model.json', sensor_id=sensor_id)
    readings = get_data_from_sensor_id(filename='data.json', sensor_id=sensor_id)
    count = count_anomalies(readings, model[0])
    return count


def count_anomalies(readings, model):
    nsigma = model['n_sigma']
    sigma = model['sigma']
    count = 0
    means_i = model['means']
    for reading in readings:
        for ix, sample_i in enumerate(reading['samples']):
            if abs(sample_i - means_i[ix]) > nsigma * sigma:
                count += 1
    return count
