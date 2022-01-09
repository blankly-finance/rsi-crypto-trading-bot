# Binance - RSI Crypto Trading Bot 

A Crypto Trading Bot on Binance using RSI in 25 Lines 

## Getting Started

Note Python Version 3.7+ is supported

1. ``` $ pip install blankly ```
2. Ensure that you have your Binance API Keys connected, check [here](https://docs.blankly.finance/config/keys.json) for more deatils
3. ``` $ python bot.py ```
4. Woila! You have a working Binance Crypto Trading Bot that trades BTCUSDT and ETHUSDT

## Backtest Output

<div align="center">
  <img style="margin: 0 auto; padding-bottom: 15px; padding-top: 30px" width=100%" src="/backtest.png">
</div>

```
Blankly Metrics: 
Compound Annual Growth Rate (%):   1.0%
Cumulative Returns (%):            2.0%
Max Drawdown (%):                  38.0%
Variance (%):                      4.36%
Sortino Ratio:                     0.18
Sharpe Ratio:                      0.19
Calmar Ratio:                      0.16
Volatility:                        0.02
Value-at-Risk:                     305.38
Conditional Value-at-Risk:         20.38
Risk Free Return Rate:             0.0
Resampled Time:                    86400.0
```

## How does this work? 

This uses the [`blankly` package](https://github.com/Blankly-Finance/Blankly) to build a [trading strategy](https://docs.blankly.finance/core/strategy) in just 25 lines of code. 
We are able to utilize the `Blankly.Strategy` object to easily add our `rsi_price_event(price, symbol, state)` function that handles our core RSI logic that trades when RSI is less than 30 and sells when it is greater than 70.

## What is RSI?

RSI or [relative strength index](https://www.investopedia.com/terms/r/rsi.asp) is an oscillator that measures the strength of a trend (i.e. when a trend is gaining momentum or losing steam). As it oscillates, it tells us when specific upwards or downward trends are most likely to stop and reverse. This is typically found when an asset is oversold (less than 30) or overbought (greater than 70) and can be used as an indicator, in conjunction with many other metrics to produce a meaningful output. 

### Resources on RSI

[What is RSI? - Investopedia](https://www.investopedia.com/terms/r/rsi.asp)
[Implementation of RSI](https://docs.blankly.finance/metrics/indicators#rsidata-period--14-round_rsi--false-use_seriesfalse)

## Next Steps

Fork this repository, and start adding in some more [indicators](https://docs.blankly.finance/metrics/indicators) to test combinations
Take this strategy live by changing it to `s.start()` 

Join our [discord](https://discord.gg/xJAjGEAXNS) and check out our upcoming [platform](https://blankly.finance/products/platform)