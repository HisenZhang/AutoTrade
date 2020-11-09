from util.config import ConfigWrapepr
from logger.loggerWrapper import Logger
from broker.webull import WebullWrapper, WebullTextView

cfg = ConfigWrapepr()
logger = Logger(cfg, 'root')
broker = WebullWrapper(logger)


if broker.login():
    v = WebullTextView(broker)
    v.printPortfolio()
    v.printPosition()
    broker.logout()
