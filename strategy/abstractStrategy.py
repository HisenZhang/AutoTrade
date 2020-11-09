from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    """
    Interface for trade strategy
    """

    @abstractmethod
    def initialize(self, context):
        """
        Run only once at setup
        """
        raise NotImplementedError

    @abstractmethod
    def before(self, context):
        """
        Once every day before trade hours
        """
        raise NotImplementedError

    @abstractmethod
    def tradeHours(self, context):
        """
        During the trade hours
        """
        raise NotImplementedError

    @abstractmethod
    def after(self, context):
        """
        Once every day after trade hours
        """
        raise NotImplementedError
