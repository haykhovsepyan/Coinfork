#from static import Static
import urllib2
import json
from collections import OrderedDict

class coin_wallets():
    def __init__(self, w_comp_buy, w_check):
        self.wallet_hitt = 'https://api.hitbtc.com/api/2/public/currency'
        self.wallet_bitt = 'https://bittrex.com/api/v1.1/public/getcurrencies'
        self.wallet_binance = 'https://www.binance.com/assetWithdraw/getAllAsset.html'
        self.responsehit = urllib2.urlopen(self.wallet_hitt)
        self.responsebitt = urllib2.urlopen(self.wallet_bitt)
        self.responsebinance = urllib2.urlopen(self.wallet_binance)
        self.hitbtcwallet = json.load(self.responsehit, object_pairs_hook=OrderedDict)
        self.bittrexwallet = json.load(self.responsebitt, object_pairs_hook=OrderedDict)
        self.binancewallet = json.load(self.responsebinance, object_pairs_hook=OrderedDict)
        self.w_comp_buy = w_comp_buy
        self.w_check = w_check



    def w_buy_sell(self, match_item):
        if self.w_check == 'hitbtc-bittrex':
            for w in self.hitbtcwallet:
                if match_item[:-3].upper() == w['id'] and w['payoutEnabled'] is True and w['payinEnabled'] is True:
                    for bw in  self.bittrexwallet['result']:
                        if bw['IsActive'] is True and match_item[:-3].upper() == bw['Currency']:
                            if self.w_comp_buy == 'hitbtc':
                                try:
                                    self.fee = float(w['payoutFee'])
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'bittrex':
                                try:
                                    self.fee = bw['TxFee']
                                except KeyError:
                                    continue
                        
                            return True

        if self.w_check == 'bittrex-binance':
            for w in self.bittrexwallet['result']:
                if w['IsActive'] is True and match_item[:-3].upper() == w['Currency']:
                    for bn in  self.binancewallet:
                        if bn['enableWithdraw'] is True and bn['enableCharge'] is True and  match_item[:-3].upper() == bn['assetCode']:
                             if self.w_comp_buy == 'bittrex':
                                try:
                                    self.fee = w['TxFee']
                                except KeyError:
                                    continue
                             if self.w_comp_buy == 'binance':
                                try:
                                    self.fee = bn['transactionFee']
                                except KeyError:
                                    continue
                             return True

        if self.w_check == 'hitbtc-binance':
            for w in self.hitbtcwallet:
                if match_item[:-3].upper() == w['id'] and w['payoutEnabled'] is True and w['payinEnabled'] is True:
                    for bn in  self.binancewallet:
                        if bn['enableWithdraw'] is True and bn['enableCharge'] is True and  match_item[:-3].upper() == bn['assetCode']:
                            if self.w_comp_buy == 'hitbtc':
                                try:
                                    self.fee = float(w['payoutFee'])
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'binance':
                                try:
                                    self.fee = bn['transactionFee']
                                except KeyError:
                                    continue
                            return True




