import argparse

class Static():
    def __init__(self, comp_path):
        self.parser = argparse.ArgumentParser(description="Coin Fork.")
        self.parser.add_argument("--btc", type=float,default=0.1,help='Btc size to buy currency, (default: %(default)s)')
        self.parser.add_argument("--perc", type=float,default=0,help='Percent difference, (default: Higher %(default)s)')
        self.args = self.parser.parse_args()
        self.size_count = 0
        self.total_count = 0
        self.btc_size = self.args.btc
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

        if comp_path == 'bittrex-poloniex':
            self.path1 = 'coinlist/bitorder'
            self.path2 = 'coinlist/poloorder'
            self.desc = '(Buy in Bittrex sell in  Poloniex)'


        if comp_path == 'poloniex-bittrex':
            self.path1 = 'coinlist/poloorder'
            self.path2 = 'coinlist/bitorder'
            self.desc = '(Buy in Poloniex sell in  Bittrex)'

            
        if comp_path == 'hitbtc-poloniex':
            self.path1 = 'coinlist/hitorder'
            self.path2 = 'coinlist/poloorder'
            self.desc = '(Buy in Hitbtc sell in  Poloniex)'


        if comp_path == 'poloniex-hitbtc':
            self.path1 = 'coinlist/poloorder'
            self.path2 = 'coinlist/hitorder'
            self.desc = '(Buy in Poloniex sell in  Hitbtc)'

        if comp_path == 'poloniex-binance':
            self.path1 = 'coinlist/poloorder'
            self.path2 = 'coinlist/binanceorder'
            self.desc = '(Buy in Poloniex sell in  Binance)'


        if comp_path == 'binance-poloniex':
            self.path1 = 'coinlist/binanceorder'
            self.path2 = 'coinlist/poloorder'
            self.desc = '(Buy in Binance sell in  Poloniex)'

        if comp_path == 'binance-exmo':
            self.path1 = 'coinlist/binanceorder'
            self.path2 = 'coinlist/exmoorder'
            self.desc = '(Buy in Binance sell in  Exmo)'

        if comp_path == 'exmo-binance':
            self.path1 = 'coinlist/exmoorder'
            self.path2 = 'coinlist/binanceorder'
            self.desc = '(Buy in Exmo sell in  Binance)'

        if comp_path == 'poloniex-exmo':
            self.path1 = 'coinlist/poloorder'
            self.path2 = 'coinlist/exmoorder'
            self.desc = '(Buy in Poloniex sell in Exmo)'


        if comp_path == 'exmo-poloniex':
            self.path1 = 'coinlist/exmoorder'
            self.path2 = 'coinlist/poloorder'
            self.desc = '(Buy in Exmo sell in  Poloniex)'

        if comp_path == 'exmo-bittrex':
            self.path1 = 'coinlist/exmoorder'
            self.path2 = 'coinlist/bitorder'
            self.desc = '(Buy in Exmo sell in  Bittrex)'

        if comp_path == 'bittrex-exmo':
            self.path1 = 'coinlist/bitorder'
            self.path2 = 'coinlist/exmoorder'
            self.desc = '(Buy in Bittrex sell in  Exmo)'


        if comp_path == 'exmo-hitbtc':
            self.path1 = 'coinlist/exmoorder'
            self.path2 = 'coinlist/hitorder'
            self.desc = '(Buy in Exmo sell in  Hitbtc)'

        if comp_path == 'hitbtc-exmo':
            self.path1 = 'coinlist/hitorder'
            self.path2 = 'coinlist/exmoorder'
            self.desc = '(Buy in HitBtc sell in  Exmo)'

