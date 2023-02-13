"""
Binance Crypto Trading Bot Based on RSI Crossover

This creates a crypto trading bot that buys BTC and ETH when RSI is less than 30 and sells
when RSI is greater than 70. Easily backtest and take this live by changing a few
lines of code.

For more information on the blankly package, check out https://docs.blankly.finance

Happy Building :D 

NOTE: Make sure you properly set your binance_tld in the `settings.json`
NOTE: Set use_sandbox = False since you will want to use Binance Live Data
"""

from blankly import Binance, Strategy, StrategyState
from blankly.utils import trunc
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
        qty = trunc(state.interface.cash * 0.5 / price, 2)
        state.interface.market_order(symbol, side='buy', size=qty)
        state.variables['owns_position'] = True
    elif rsi_output[-1] > 70 and state.variables['owns_position']:
        # get the amount of bitcoin we have in our account
        curr_value = trunc(state.interface.account[state.base_asset].available, 2)
        state.interface.market_order(symbol, side='sell', size=curr_value)
        state.variables['owns_position'] = False
    
exchange = Binance()
strategy = Strategy(exchange)

strategy.add_price_event(rsi_price_event, symbol='BTC-USDT', resolution='1h', init=init)
strategy.add_price_event(rsi_price_event, symbol='ETH-USDT', resolution='1h', init=init)

if blankly.is_deployed:
    strategy.start()
else:
    results = strategy.backtest(to='2y', initial_values={'USDT': 10000})
    print(results)
