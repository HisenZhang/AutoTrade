from abc import ABC, abstractmethod


class BrokerAdaptor(ABC):
    """
    Interface for brokers
    """
    @abstractmethod
    def position(self):
        """
        Get positions
        """
        raise NotImplementedError

    @abstractmethod
    def account(self):
        """
        Get account summary
        """
        raise NotImplementedError

    @abstractmethod
    def portfolio(self):
        """
        Get portfolio
        """
        raise NotImplementedError

    @abstractmethod
    def position(self):
        """
        Show account position
        """
        raise NotImplementedError

    @abstractmethod
    def buy(self, sec, qty):
        """
        Buy stock
        """
        raise NotImplementedError

    @abstractmethod
    def sell(self, sec, qty):
        """
        Sell stock
        """
        raise NotImplementedError

    @abstractmethod
    def modify(self):
        """
        Modify order
        """
        raise NotImplementedError

    @abstractmethod
    def cancel(self):
        """
        Cancel order
        """
        raise NotImplementedError

    @abstractmethod
    def cancelAll(self):
        """
        Cancel all orders
        """
        raise NotImplementedError

    @abstractmethod
    def quote(self):
        """
        Get quote
        """
        raise NotImplementedError

    @abstractmethod
    def login(self) -> bool:
        """
        Login to server
        """
        raise NotImplementedError

    @abstractmethod
    def logout(self) -> bool:
        """
        Logout
        """
        raise NotImplementedError
