from logger.loggerWrapper import logger
from broker.webull import WebullWrapper, WebullTextView


broker = WebullWrapper(logger)
textView = None


while True:
    s = input('>>> ').lower()
    if s == 'q':
        broker.logout()
        break
    if s == 'l':
        if broker.login():
            textView = WebullTextView(broker)
    if s == 'p':
        textView.printPosition()
    if s == 's':
        textView.printPortfolio()
    if s == 'h':
        print("Quit Summary Position")
