class Component():
    def __init__(self, component_buy, component_sell):
        self.component_buy = component_buy
        self.component_sell = component_sell
    def comp_buy_sell(self, data_js_buy, data_js_sell):
        try:
            if self.component_buy == 'bittrex':
                self.data_to_loop = data_js_buy['result']['sell']
                self.price_key = 'Rate'
                self.size_key = 'Quantity'
                self.total_key = None

            elif  self.component_buy == 'binance' or self.component_buy == 'poloniex':
                self.data_to_loop = data_js_buy['asks']
                self.price_key = 0
                self.size_key = 1
                self.total_key = None

            else:
                self.data_to_loop = data_js_buy['ask']
                self.price_key = 'price'
                self.size_key = 'size'
                self.total_key = None

            if self.component_sell == 'bittrex_sell':
                self.data_to_sell = data_js_sell['result']['buy']
                self.price_key_sell = 'Rate'
                self.size_key_sell = 'Quantity'
                self.total_key_sell = None

            elif  self.component_sell == 'binance_sell' or self.component_sell == 'poloniex_sell':
                self.data_to_sell = data_js_sell['bids']
                self.price_key_sell = 0
                self.size_key_sell = 1
                self.total_key_sell = None
            else:
                self.data_to_sell = data_js_sell['bid']
                self.price_key_sell = 'price'
                self.size_key_sell = 'size'
                self.total_key_sell = None

        except TypeError:
            return False




