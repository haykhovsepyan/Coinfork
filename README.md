# Coinfork
**Coin fork  between exchanges**

Coin Fork is  scrypt wrote in python 2.7, that find fork between exchanges Poloniex, Hitbtc, Binance, Exmo and Bittrex.
Scrypt is working only with BTC compare , by  BTC size (Size BTC passes via argument) buys currency in one exchange  and sell in other exchange.

Buy Sell works with open orders (asks, bid), checks if withdraw and deposit is  True, count Tax Fee and get result by percent different that you also can pass via argument.

Arguments:

--btc BTC    Btc size to buy currency, (default: 0.1)<br/>
--perc PERC  Percent difference, (default: Higher 0)


**Example:**

**python fork.py --btc 0.5 --perc 2**

('6.73%', 'emcbtc-(Buy in HitBtc sell in  Bittrex)')

The result, script  buy Emercoin in Hitbtc for 0.5 BTC, then sell in Bittrex  and  get difference higher 2%.


  
