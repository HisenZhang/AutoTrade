from configparser import ConfigParser, RawConfigParser, NoOptionError
import os.path


class ConfigParser(RawConfigParser):
    """
    Overload deault bahavior of library method
    """

    def get(self, section, option):
        try:
            return RawConfigParser.get(self, section, option)
        except NoOptionError:
            return None


class ConfigWrapepr(object):
    """
    Access config
    """

    def __init__(self):
        self.parser = ConfigParser(allow_no_value=True)
        configFile = 'globalConfig.ini'
        self.parser.read(configFile)

    def get(self, section: str, key: str):
        return self.parser.get(section, key)

    def set(self, section: str, key: str):
        return self.parser.set(section, key)
