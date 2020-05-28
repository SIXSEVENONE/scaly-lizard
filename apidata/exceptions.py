class VKApiException(Exception):
    def __init__(self, status_code):
        if status_code < 200:
            message = f"Oopes! Got an informational message by code: {status_code}"
        elif status_code >= 300 and status_code <400:
            message = f"Oppes! Got a Redirection error by code: {status_code}"
        elif status_code == 403:
            message = f"Rate limit exceeded. Error {status_code}."
        elif status_code >= 400 and status_code <500 and status_code != 403:
            message = f"Oppes! Got a Client error by code: {status_code}"
        elif status_code >= 500:
            message = f"Oppes! Got a Server error by code: {status_code}"
        super().__init__(message)
        