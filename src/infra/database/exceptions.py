class DbException(Exception):
    def __init__(self, message: str):
        super(DbException, self).__init__(message)
        self.error = "Unknown"
        self.message = message
