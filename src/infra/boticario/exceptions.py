class BoticarioException(Exception):
    def __init__(self, message: str, status_code: int):
        super(BoticarioException, self).__init__(message)
        self.error = "Unknown"
        self.message = message
        self.status_code = status_code


class BoticarioRequestException(BoticarioException):
    def __init__(self, error: str, message: str, status_code: int):
        super(BoticarioRequestException, self).__init__(message, status_code)
        self.error = error
        self.message = message
        self.status_code = status_code
