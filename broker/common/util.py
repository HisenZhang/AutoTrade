from configparser import ConfigParser, RawConfigParser, NoOptionError
import os.path


class AutoTradeException(Exception):
    """
    Base exception for all 
    """
    pass


class LoginFailure(AutoTradeException):
    """
    Login failure 
    """

    def __init__(self, msg: str, code: str, traceId: str):
        self.msg = msg
        self.code = code
        self.traceId = traceId
        pass


class BrokerConfigParser(RawConfigParser):
    """
    Overload deault bahavior of library method
    """

    def get(self, section, option):
        try:
            return RawConfigParser.get(self, section, option)
        except NoOptionError:
            return None


class BrokerConfigWrapper(object):
    """
    Access credentials
    """

    def __init__(self, broker: str):
        self.parser = BrokerConfigParser(allow_no_value=True)
        configFile = os.path.join(
            'broker', 'common', 'brokerConfig.ini')
        self.parser.read(configFile)

        self.username = self.parser.get(broker, 'username')
        self.password = self.parser.get(broker, 'password')

    def get(self, broker: str, key: str):
        return self.parser.get(broker, key)

    def set(self, broker: str, key: str):
        return self.parser.set(broker, key)
