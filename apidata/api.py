import requests
from apidata.exceptions import VKApiException

VK_API_URL_1 = ''












if response.status_code < 200 or response.status_code >= 300:
    raise VKApiException(response.status_code)