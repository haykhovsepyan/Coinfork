# Coinfork
Coin fork  between exchanges

Coin Fork is  scrypt wrote in python 2.7, that find fork between exchanges Poloniex, Hitbtc, Binance and Bittrex.
Scrypt is working only with BTC compare , by  BTC size (Size BTC passes via argument) buys currency in one exchange  and sell in other exchange.

Buy Sell works with open orders (asks, bid) and get result by percent different that you also can pass via argument.

Arguments:

--btc BTC    Btc size to buy currency, (default: 0.1)
--perc PERC  Percent difference, (default: Higher 0)


Example:

python fork.py --btc 0.5 --perc 2 

buys currencies for 0.5 BTC and shows result that gets difference higher 2%.


  
