from scripts.assets import Stock, Account

class Moving_average_bot:
  '''
  past n day moving average bot

  '''
  def __init__(self, stock, balance, n = 20):
    self.stock = stock
    self.balance = balance
    self.shares = 0
    self.n = n

  def make_decision (self):
    cur_price = self.stock.cur_price
    last_price = self.stock.past_price[0]
    moving_average = self.stock.moving_average(0, self.n)
    if last_price < moving_average and cur_price > moving_average:
      return 'buy'
    elif last_price > moving_average and cur_price < moving_average:
      return 'sell'
    else:
      return 'stay'



  
class Macd_bot:
  def __init__(self,stock, balance):
    self.stock = stock
    self.balance = balance
    self.shares = 0

  def make_decision(self):
    arr = self.stock.past_price
    cur = self.stock.cur_price
    yesterday = self.stock.past_price[0]
    current_macd = self.stock.macd(self, cur, arr)
    yesterday_macd = self.stock.macd(self, yesterday, arr[1:])
    if current_macd > 0 and yesterday_macd < 0:
      return 'buy'
    elif current_macd < 0 and yesterday_macd > 0:
      return 'sell'
    else:
      return 'stay'