import urllib2
import json
import ast
from collections import OrderedDict
from static import Static
from component import Component
from wallet import coin_wallets

def coin_list(lists):
    with open(lists, 'r') as coins:
        s = coins.read()
        birja = ast.literal_eval(s)
        return birja
    
def parse_js(settings, buysell, wallets):
    path1 = settings.path1
    path2 = settings.path2
    market1 = coin_list(path1)
    market2 = coin_list(path2)
    for match_item, market_url in market2.iteritems():
        if match_item in market1:
            try:
                response_market1 = urllib2.urlopen(market1[match_item])
                response_market2 = urllib2.urlopen(market_url)

                response_text_market1 = response_market1.read()
                response_text_market2 = response_market2.read()
                data_js_buy = json.loads(response_text_market1)
                data_js_sell = json.loads(response_text_market2)
            except urllib2.HTTPError,  err:
                continue
            perc = get_percent(settings, data_js_buy, data_js_sell, match_item, buysell, wallets)
            if perc:
                print perc
            

def coin_buy(data_js_buy, data_js_sell, settings,  buysell, match_item, wallets):
    wallets.w_buy_sell(match_item)
    buysell.comp_buy_sell(data_js_buy, data_js_sell)
    if wallets.w_buy_sell(match_item) and buysell.comp_buy_sell(data_js_buy, data_js_sell) is not False:
        btc_size = settings.btc_size
        size_count = settings.size_count
        total_count = settings.total_count
        for index, item in enumerate(buysell.data_to_loop):
            price = float(item[buysell.price_key])
            size = float(item[buysell.size_key])
            count = len(buysell.data_to_loop)
            if buysell.total_key:
                total = float(item[buysell.total_key])
            else:
                total = price * size
            
            btc_size -= total
            size_count += size
            if btc_size <= 0:
                global size_total
                size_total = btc_size / price + size_count - wallets.fee
                break
        
        try:
            return size_total
        except NameError:
             return False




def coin_sell(data_js_sell, settings,  data_js_buy, match_item, buysell, wallets):
    size_total = coin_buy(data_js_buy, data_js_sell, settings,  buysell, match_item, wallets)
    if size_total:
        total_count_sell = settings.total_count_sell
        size_count_sell = settings.size_count_sell
        for index, item in enumerate(buysell.data_to_sell):
            price_sell = float(item[buysell.price_key_sell])
            size_sell = float(item[buysell.size_key_sell])
            if buysell.total_key_sell:
                total_sell = float(item[buysell.total_key_sell])
            else:
                total_sell = price_sell * size_sell
            

            size_total -= size_sell
            total_count_sell += total_sell
            if size_total <=0:
                global sell_result
                sell_result = size_total * price_sell + total_count_sell
                break

        try:
            return sell_result
        except NameError:
            return False



            
    
def get_percent(settings, data_js_buy, data_js_sell, match_item, buysell, wallets):
    sell = coin_sell(data_js_sell, settings, data_js_buy, match_item, buysell, wallets)
    if sell:
        fork_desc = "%s-%s" % (match_item, settings.desc)
        perc_result = 100 - (100 * settings.btc_size) / sell
        if perc_result > settings.percent_limit:
            result = str("%.2f" % perc_result) + '%', fork_desc, #'\n'
            return result


