"""
Binance Crypto Trading Bot Based on RSI Crossover

This creates a crypto trading bot that buys when RSI is less than 30 and sells
when RSI is greater than 70. Easily backtest and take this live by changing a few
lines of code.

For more information on the blankly package, check out https://docs.blankly.finance

Happy Building :D 

NOTE: Make sure you properly set your binance_tld in the `settings.json`
"""

from blankly import Binance, Strategy, StrategyState
from blankly.indicators import rsi

def init(symbol, state: StrategyState):
    state.variables['history'] = state.interface.history(symbol, to=150, 
        resolution=state.resolution, 
        return_as='deque')['close']
    state.variables['owns_position'] = False

def rsi_price_event(price, symbol, state: StrategyState):
    state.variables['history'].append(price) # appends to the deque of historical prices
    rsi_output = rsi(state.variables['history'])
    if rsi_output[-1] < 30 and not state.variables['owns_position']:
        buy = int(state.interface.cash / price)
        state.interface.market_order(symbol, side='buy', size=buy)
        state.variables['owns_position'] = True
    elif rsi_output[-1] > 70 and state.variables['owns_position']:
        # get the amount of bitcoin we have in our account
        curr_value = int(state.interface.account[state.base_asset].available)
        state.interface.market_order(symbol, side='sell', size=curr_value)
        state.variables['owns_position'] = False
    
exchange = Binance()
strategy = Strategy(exchange)

strategy.add_price_event(rsi_price_event, symbol='BTC-USDT', resolution='1d', init=init)

results = strategy.backtest(to='1y', initial_values={'USDT': 10000})
print(results)

# Take this strategy live by uncommenting this line
# strategy.start()