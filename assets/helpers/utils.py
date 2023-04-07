import requests
from assets.values.test_values import Urls


def epoch_request(epoch, date_time_string, response_code=200):
    epoch_datetime = epoch
    response = requests.get("{}{}".format(Urls.epoch_api_url, epoch_datetime))
    assert response.status_code == response_code, "{} does not equal {}".format(response.status_code, response_code)
    assert response.text == date_time_string, "{} does not equal {}".format(response.text, date_time_string)
