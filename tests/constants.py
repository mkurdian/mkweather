import os


JSON_RESPONSE = {
    "coord": {
        "lon": -0.13,
        "lat": 51.51
    },
    "weather": [
        {
            "id": 500,
            "main": "Rain",
            "description": "light rain",
            "icon": "10d"
        }
    ],
    "base": "stations",
    "main": {
            "temp": 22.89,
            "feels_like": 25.32,
            "temp_min": 21.67,
            "temp_max": 24.44,
            "pressure": 1012,
            "humidity": 79
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.18,
        "deg": 54
    },
    "rain": {
        "1h": 0.58
    },
    "clouds": {
        "all": 81
    },
    "dt": 1597575032,
    "sys": {
        "type": 3,
        "id": 2019646,
        "country": "GB",
        "sunrise": 1597553297,
        "sunset": 1597605688
    },
    "timezone": 3600,
    "id": 2643743,
    "name": "London",
    "cod": 200
}

SKIP_INTEGRATION_TEST = os.getenv('SKIP_INTEGRATION_TEST', True)
