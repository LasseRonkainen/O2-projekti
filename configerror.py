class ConfigError(Exception):

    def __init__(self, message):
        super(ConfigError, self).__init__(message)