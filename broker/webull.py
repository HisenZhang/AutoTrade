from webull import webull
from .common.adaptor import BrokerAdaptor
from .common.util import *
from prettytable import PrettyTable


class WellbullConfig(BrokerConfigWrapper):
    """
    Config for webull
    """

    def __init__(self):

        import os.path
        self.broker = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(self.broker)

        self.deviceName = self.parser.get(self.broker, 'deviceName')

        self.access_token = self.parser.get(self.broker, 'access_token')
        self.refresh_token = self.parser.get(self.broker, 'refresh_token')
        self.token_expire = self.parser.get(self.broker, 'token_expire')
        self.uuid = self.parser.get(self.broker, 'uuid')
        pass

    def get(self, key: str):
        return self.parser.get(self.broker, key)

    def set(self, key: str):
        return self.parser.set(self.broker, key)


class WebullWrapper(BrokerAdaptor):
    """
    Wellbull wrapper
    """

    def __init__(self, logger):
        """
        Initialize wrapper
        """
        self.logger = logger
        self.config = WellbullConfig()
        self.wb = webull()
        self.online = False
        pass

    def position(self):
        """
        Get positions
        """
        return self.wb.get_positions()

    def account(self):
        """
        Get account summary
        """
        return self.wb.get_account()

    def portfolio(self):
        """
        Get portfolio
        """
        return self.wb.get_portfolio()

    def buy(self, sec, qty):
        """
        Buy stock
        """
        pass

    def sell(self, sec, qty):
        """
        Sell stock
        """
        raise NotImplementedError

    def order(self, sec, qty):
        """
        List order
        """
        raise NotImplementedError

    def modify(self):
        """
        Modify order
        """
        raise NotImplementedError

    def cancel(self):
        """
        Cancel order
        """
        raise NotImplementedError

    def cancelAll(self):
        """
        Cancel all orders
        """
        raise NotImplementedError

    def quote(self):
        """
        Get quote
        """
        raise NotImplementedError

    def login(self) -> bool:
        """
        Login to server
        """
        if self.online:
            self.logger.warning("Already logged in as " + self.wb._account_id)
            return False
        try:
            loginInfo = str()
            if self.config.access_token:
                loginInfo = self.wb.api_login(
                    self.config.access_token,
                    self.config.refresh_token,
                    self.config.token_expire,
                    self.config.uuid)
            else:
                loginInfo = self.wb.login(
                    self.config.username,
                    self.config.password,
                    self.config.deviceName)

            # Login error
            if 'code' in loginInfo.keys():
                raise LoginFailure(
                    loginInfo['msg'],
                    loginInfo['code'],
                    loginInfo['traceId'])

        except LoginFailure as e:
            args = e.args
            self.logger.error('Login failed: ' +
                              ' '.join((args.msg,
                                        args.code,
                                        args.traceId)))
            return False

        except Exception as e:
            self.logger.error("Login failed. " + repr(e))
            return False

        else:
            self.online = True
            self.logger.info('Logged in. ')

            self.config.set(loginInfo['accessToken'])
            self.config.set(loginInfo['uuid'])
            self.config.set(loginInfo['refreshToken'])
            self.config.set(loginInfo['tokenExpireTime'])

            return True

            # ' '.join((loginInfo['accessToken'],
            #            loginInfo['uuid'],
            #            loginInfo['refreshToken'],
            #            loginInfo['tokenExpireTime']))
            # ' '.join(
            #     (account['secAccountId'],
            #      account['brokerId'],
            #      account['accountType'],
            #      account['brokerAccountId']))

    def logout(self) -> bool:
        if not self.online:
            self.logger.warn("Not connected to any account yet.")
            return False
        try:
            code = self.wb.logout()
            assert (code == 200)
        except AssertionError as e:
            self.logger.error("Logout failed.")
            return False
        else:
            self.online = False
            self.logger.info("Logged out.")
            return True


class WebullTextView(object):
    """
    Text view for Webull
    """

    def __init__(self, wrapper: WebullWrapper):
        self.model = wrapper
        pass

    def printPosition(self, sortBy="Float Profit/Loss", reverse=True):
        """
        Show account position
        """
        x = PrettyTable()
        x.field_names = ["Symbol",
                         "Position",
                         "Market Value",
                         "Cost",
                         "Float Profit/Loss",
                         "Float Profit/Loss Rate",
                         "Proportion %"]
        x.align = "r"
        x.reversesort = reverse
        x.sortby = sortBy
        x.clear_rows()

        for p in self.model.position():
            x.add_row([p['ticker']['symbol'],
                       int(p['position']),
                       float(p['marketValue']),
                       float(p['cost']),
                       float(p['unrealizedProfitLoss']),
                       round(float(p['unrealizedProfitLossRate']) * 100, 2),
                       round(float(p["positionProportion"]) * 100, 2)])
        print(x)

    def printAccount(self):
        """
        Show account summary
        """
        raise NotImplementedError

    def printPortfolio(self):
        x = PrettyTable()
        x.field_names = ["Item",
                         "Value"]
        x.clear_rows()

        for k, v in self.model.portfolio().items():
            x.add_row([k, v])
        print(x)
