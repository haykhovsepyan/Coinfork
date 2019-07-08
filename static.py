import urllib2
import json
from collections import OrderedDict
import argparse

class Static():
    def __init__(self, comp_path):
        self.parser = argparse.ArgumentParser(description="Coin Fork arguments descriptions.")
        #self.parser.add_argument("a")
        self.parser.add_argument("--btc", type=float,default=0.1,help='Btc size to buy coin, default 0.1BTC')
        self.parser.add_argument("--perc", type=float,default=0,help='Percent to view result, default higher 0%')
        self.args = self.parser.parse_args()
        self.size_count = 0
        self.total_count = 0
        #self.magic_number = float(self.args.a)
        self.magic_number = self.args.btc
        self.size_count_sell = 0
        self.total_count_sell = 0
        self.percent_limit = self.args.perc
        if comp_path == 'bittrex-hitbtc':
            self.path1 = 'coinlist/bitorder'
            self.path2 = 'coinlist/hitorder'
            self.desc = '(Buy in Bittrex sell in  Hitbtc)'

        if comp_path == 'hitbtc-bittrex':
            self.path1 = 'coinlist/hitorder'
            self.path2 = 'coinlist/bitorder'
            self.desc = '(Buy in HitBtc sell in  Bittrex)'

        
        if comp_path == 'bittrex-binance':
            self.path1 = 'coinlist/bitorder'
            self.path2 = 'coinlist/binanceorder'
            self.desc = '(Buy in Bittrex sell in  Binance)'


        if comp_path == 'binance-bittrex':
            self.path1 = 'coinlist/binanceorder'
            self.path2 = 'coinlist/bitorder'
            self.desc = '(Buy in Binance sell in  Bittrex)'


        if comp_path == 'hitbtc-binance':
            self.path1 = 'coinlist/hitorder'
            self.path2 = 'coinlist/binanceorder'
            self.desc = '(Buy in Hitbtc sell in  Binance)'


        if comp_path == 'binance-hitbtc':
            self.path1 = 'coinlist/binanceorder'
            self.path2 = 'coinlist/hitorder'
            self.desc = '(Buy in Binance sell in  Hitbtc)'
