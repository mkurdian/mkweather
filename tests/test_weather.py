import os
from unittest.mock import Mock, patch

import pytest
import requests

from mkweather.weather import get_weather, get_console_text
from .constants import JSON_RESPONSE, SKIP_INTEGRATION_TEST


# ---- API Request Tests ----
@patch('mkweather.weather.requests.get')
def test_get_weather_when_response_ok(mock_get):
    """
    Test for json response from successful request response.
    """
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = JSON_RESPONSE

    response = get_weather(city='london', country_code='gb')
    assert response.json() == JSON_RESPONSE


@patch('mkweather.weather.requests.get')
def test_get_weather_when_response_not_ok(mock_get):
    """
    Test for 'None' response for a unsuccessful request.
    """
    mock_get.return_value.ok = False

    response = get_weather(city='london', country_code='gb')
    assert response is None


@patch('mkweather.weather.requests.get')
def test_set_city_and_country(mock_get):
    """
    Test passing of city and country code as arguments.
    """
    city = 'las vegas'
    country_code = 'us'

    response = get_weather(city=city, country_code=country_code)

    mock_get_arguments = mock_get.call_args_list[0]._get_call_arguments()[1]
    assert mock_get_arguments['params']['q'] == f'las vegas,us'


# ---- Console Display Tests ----
@patch('mkweather.weather.get_weather')
def test_display_when_response_not_none(mock_get_weather):
    """
    Test console display output for successful request.
    """
    mock_get_weather.return_value = Mock()
    mock_get_weather.return_value.json.return_value = JSON_RESPONSE

    display_text = get_console_text(city="london", country_code="gb")

    assert mock_get_weather.called
    assert display_text == "\n\033[1mWeather:\033[0m\nLondon, GB Sun Aug 2020 12:50\n22.89˚C\nlight rain"


@patch('mkweather.weather.get_weather')
def test_display_when_response_is_none(mock_get_weather):
    """
    Test console display output for unsuccessful request.
    """
    mock_get_weather.return_value = None

    display_text = get_console_text(city="london", country_code="gb")

    assert mock_get_weather.called
    assert display_text == "Failed request."


@patch('mkweather.weather.get_weather')
def test_display_with_city_and_country_code(mock_get_weather):
    """
    Test console display text for given city and country code.
    """
    display_text = get_console_text(city='las vegas', country_code='us')
    mock_get_weather.assert_called_with(city='las vegas', country_code='us')

# ---- Integration Tests ----


@pytest.mark.skipif(SKIP_INTEGRATION_TEST, reason="skipping test that hits live web api")
def test_api_response_json_keys():
    """
    Test live response json keys match those with the mock json.
    """
    real_response = get_weather(city='london', country_code='gb')
    real_keys = list(real_response.json().keys())

    with patch('mkweather.weather.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = JSON_RESPONSE

        mock_response = get_weather(city='london', country_code='gb')
        mock_keys = list(mock_response.json().keys())

    # sometimes these keys are not returned from server
    optional_keys = ['wind', 'clouds', 'rain', 'snow']
    for key in optional_keys:
        if key in real_keys:
            real_keys.remove(key)
        if key in mock_keys:
            mock_keys.remove(key)

    assert mock_keys == real_keys
