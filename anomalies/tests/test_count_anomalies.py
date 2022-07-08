from anomalies.helper_functions import get_count_anomalies


def test_change():
    assert get_count_anomalies('cr123') == 8
