class SecureConfig(object):
    """yaml configuration parser object with protected attrs.

    Attributes:
        path (str): to where config file is

    Methods:
        __init__
        __setattr__
        _register_attrs

    """

    def __init__(self):
        """initializes configuration."""
        self._path = 'config.yml'
        with open(self._path, 'r') as stream:
            config = yaml.load(stream)

        self._register_attrs(config)

    def _register_attrs(self, config):
        """sets attributes dynamically."""
        for key in config:
            self.__dict__[key] = config[key]

