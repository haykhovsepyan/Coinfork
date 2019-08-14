from urllib.request import urlopen
import json
from collections import OrderedDict

class coin_wallets():
    def __init__(self, w_comp_buy, w_check):
        self.wallet_hitt = 'https://api.hitbtc.com/api/2/public/currency'
        self.wallet_bitt = 'https://bittrex.com/api/v1.1/public/getcurrencies'
        self.wallet_binance = 'https://www.binance.com/assetWithdraw/getAllAsset.html'
        self.wallet_poloniex = 'https://poloniex.com/public?command=returnCurrencies'
        self.exmo_fees = {'BTC':0.0005, 'LTC':0.01, 'DOGE':1, 'DASH':0.01, 'ETH':0.01, 'WAVES':0.001, 'ZEC':0.001, 'USDT':5, 'XMR':0.001, 'XRP':0.02, 'KICK':50, 'ETC':0.01, 'BCH':0.001, 'BTG':0.001, 'HBZ':65, 'DXT':20, 'STQ':100, 'XLM':0.01, 'MNX':0.01, 'OMG':0.5, 'TRX':1, 'ADA':1, 'INK':50, 'NEO':0, 'GAS':0, 'ZRX':1, 'GNT':1, 'GUSD':0.5, 'XEM':5, 'SMART':0.5, 'QTUM':0.01, 'HB':10, 'DAI':1, 'MKR':0.005, 'MNC':15, 'ATMCASH':5, 'ETZ':1, 'USDC':0.5, 'DCR':0.01}
        self.responsehit = urlopen(self.wallet_hitt)
        self.responsebitt = urlopen(self.wallet_bitt)
        self.responsebinance = urlopen(self.wallet_binance)
        self.responsepolo = urlopen(self.wallet_poloniex)
        self.hitbtcwallet = json.load(self.responsehit, object_pairs_hook=OrderedDict)
        self.bittrexwallet = json.load(self.responsebitt, object_pairs_hook=OrderedDict)
        self.binancewallet = json.load(self.responsebinance, object_pairs_hook=OrderedDict)
        self.polowallet = json.load(self.responsepolo, object_pairs_hook=OrderedDict)
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

        if self.w_check == 'bittrex-poloniex':
            for w in self.bittrexwallet['result']:
                if w['IsActive'] is True and match_item[:-3].upper() == w['Currency']:
                    for p_item, p_url in self.polowallet.items():
                        if match_item[:-3].upper() == p_item and p_url['disabled'] == 0 and p_url['delisted'] == 0 and p_url['frozen'] == 0:
                            if self.w_comp_buy == 'bittrex':
                                try:
                                    self.fee = w['TxFee']
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'poloniex':
                                try:
                                    self.fee = float(p_url['txFee'])
                                except KeyError:
                                    continue
                            return True


        if self.w_check == 'hitbtc-poloniex':
            for h in self.hitbtcwallet:
                if match_item[:-3].upper() == h['id'] and h['payoutEnabled'] is True and h['payinEnabled'] is True:
                    for p_item, p_url in self.polowallet.items():
                        if match_item[:-3].upper() == p_item and p_url['disabled'] == 0 and p_url['delisted'] == 0 and p_url['frozen'] == 0:
                            if self.w_comp_buy == 'hitbtc':
                                try:
                                    self.fee = float(h['payoutFee'])
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'poloniex':
                                try:
                                    self.fee = float(p_url['txFee'])
                                except KeyError:
                                    continue
                            return True

        if self.w_check == 'binance-poloniex': 
            for bn in  self.binancewallet:
                if bn['enableWithdraw'] is True and bn['enableCharge'] is True and  match_item[:-3].upper() == bn['assetCode']:
                    for p_item, p_url in self.polowallet.items():
                        if match_item[:-3].upper() == p_item and p_url['disabled'] == 0 and p_url['delisted'] == 0 and p_url['frozen'] == 0:
                            if self.w_comp_buy == 'binance':
                                try:
                                    self.fee = bn['transactionFee']
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'poloniex':
                                try:
                                    self.fee = float(p_url['txFee'])
                                except KeyError:
                                    continue
                            return True


        if self.w_check == 'binance-exmo':
            for bn in  self.binancewallet:
                if bn['enableWithdraw'] is True and bn['enableCharge'] is True and  match_item[:-3].upper() == bn['assetCode']:
                    for ex_item, ex_fee in self.exmo_fees.items():
                        if match_item[:-3].upper() == ex_item:
                            if self.w_comp_buy == 'binance':
                                try:
                                    self.fee = bn['transactionFee']
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'exmo':
                                try:
                                    self.fee = ex_fee
                                except KeyError:
                                    continue
                            return True

        if self.w_check == 'exmo-poloniex':
            for ex_item, ex_fee in self.exmo_fees.items():
                if match_item[:-3].upper() == ex_item:
                    for p_item, p_url in self.polowallet.items():
                        if match_item[:-3].upper() == p_item and p_url['disabled'] == 0 and p_url['delisted'] == 0 and p_url['frozen'] == 0:
                            if self.w_comp_buy == 'exmo':
                                try:
                                    self.fee = ex_fee
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'poloniex':
                                try:
                                    self.fee = float(p_url['txFee'])
                                except KeyError:
                                    continue
                            return True


        if self.w_check == 'hitbtc-exmo':
            for h in self.hitbtcwallet:
                if match_item[:-3].upper() == h['id'] and h['payoutEnabled'] is True and h['payinEnabled'] is True:
                    for ex_item, ex_fee in self.exmo_fees.items():
                        if match_item[:-3].upper() == ex_item:
                            if self.w_comp_buy == 'hitbtc':
                                try:
                                    self.fee = float(h['payoutFee'])
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'exmo':
                                try:
                                    self.fee = ex_fee
                                except KeyError:
                                    continue
                            return True




        if self.w_check == 'bittrex-exmo':
            for w in self.bittrexwallet['result']:
                if w['IsActive'] is True and match_item[:-3].upper() == w['Currency']:
                    for ex_item, ex_fee in self.exmo_fees.items():
                        if match_item[:-3].upper() == ex_item:
                            if self.w_comp_buy == 'bittrex':
                                try:
                                    self.fee = w['TxFee']
                                except KeyError:
                                    continue
                            if self.w_comp_buy == 'exmo':
                                try:
                                    self.fee = ex_fee
                                except KeyError:
                                    continue
                            return True

