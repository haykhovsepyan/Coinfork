import func as fc
from static import Static
from component import Component
from wallet import coin_wallets


def run_fork():
    ### By in Bittrex Sell in Hitbtc ###
    settings_bittrex_hitbtc = Static('bittrex-hitbtc')
    buysell_bittrex_hitbtc = Component('bittrex', 'hitbtc_sell')
    wallets_bittrex_hitbtc = coin_wallets('bittrex', 'hitbtc-bittrex')
    fc.parse_js(settings_bittrex_hitbtc, buysell_bittrex_hitbtc, wallets_bittrex_hitbtc)

    ### By in Hitbtc sell in Bittrex ###
    settings_hitbtc_bittrex = Static('hitbtc-bittrex')
    buysell_hitbtc_bittrex = Component('hitbtc', 'bittrex_sell')
    wallets_hitbtc_bittrex = coin_wallets('hitbtc', 'hitbtc-bittrex')
    fc.parse_js(settings_hitbtc_bittrex, buysell_hitbtc_bittrex, wallets_hitbtc_bittrex)
    
    ### Buy in Bittrex sell in Binance ###
    settings_bittrex_binance = Static('bittrex-binance')
    buysell_bittrex_binance = Component('bittrex', 'binance_sell')
    wallets_bittrex_binance = coin_wallets('bittrex', 'bittrex-binance')
    fc.parse_js(settings_bittrex_binance, buysell_bittrex_binance, wallets_bittrex_binance)

    ### Buy in Binance Sell in Bittrex ###
    settings_binance_bittrex = Static('binance-bittrex')
    buysell_binance_bittrex = Component('binance', 'bittrex_sell')
    wallets_binance_bittrex = coin_wallets('binance', 'bittrex-binance')
    fc.parse_js(settings_binance_bittrex, buysell_binance_bittrex, wallets_binance_bittrex)

    ### Buy in HitBtc Sell in Binance ###
    settings_hitbtc_binance =  Static('hitbtc-binance')
    buysell_hitbtc_binance = Component('hitbtc', 'binance_sell')
    wallets_hitbtc_binance = coin_wallets('hitbtc', 'hitbtc-binance')
    fc.parse_js(settings_hitbtc_binance, buysell_hitbtc_binance, wallets_hitbtc_binance)

    ### Buy in Binance Sell in Hitbtc ###
    settings_binance_hitbtc = Static('binance-hitbtc')
    buysell_binance_hitbtc = Component('binance', 'hitbtc_sell')
    wallets_binance_hitbtc = coin_wallets('binance', 'hitbtc-binance')
    fc.parse_js(settings_binance_hitbtc, buysell_binance_hitbtc, wallets_binance_hitbtc)


    ### Buy in Bittrex Sell in Poloniex ###
    settings_bittrex_polo = Static('bittrex-poloniex')
    buysell_bittrex_polo = Component('bittrex', 'poloniex_sell')
    wallets_bittrex_polo = coin_wallets('bittrex', 'bittrex-poloniex')
    fc.parse_js(settings_bittrex_polo, buysell_bittrex_polo, wallets_bittrex_polo)


    ### Buy in Poloniex Sell in Bittrex ###
    settings_polo_bittrex = Static('poloniex-bittrex')
    buysell_polo_bittrex = Component('poloniex', 'bittrex_sell')
    wallets_polo_bittrex = coin_wallets('poloniex', 'bittrex-poloniex')
    fc.parse_js(settings_polo_bittrex, buysell_polo_bittrex, wallets_polo_bittrex)

    ### Buy in Binance Sell in Poloniex ###
    settings_binance_polo = Static('binance-poloniex')
    buysell_binance_polo = Component('binance', 'poloniex_sell')
    wallets_binance_polo = coin_wallets('binance', 'binance-poloniex')
    fc.parse_js(settings_binance_polo, buysell_binance_polo, wallets_binance_polo)


    ### Buy in Poloniex Sell in Binance ###
    settings_polo_binance = Static('poloniex-binance')
    buysell_polo_binance = Component('poloniex', 'binance_sell')
    wallets_polo_binance = coin_wallets('poloniex', 'binance-poloniex')
    fc.parse_js(settings_polo_binance, buysell_polo_binance, wallets_polo_binance)

    ### Buy in HitBtc Sell in Poloniex ###
    settings_hitbtc_polo =  Static('hitbtc-poloniex')
    buysell_hitbtc_polo = Component('hitbtc', 'poloniex_sell')
    wallets_hitbtc_polo = coin_wallets('hitbtc', 'hitbtc-poloniex')
    fc.parse_js(settings_hitbtc_polo, buysell_hitbtc_polo, wallets_hitbtc_polo)


    ### Buy in Poloniex Sell in Hitbtc ###
    settings_polo_hitbtc =  Static('poloniex-hitbtc')
    buysell_polo_hitbtc = Component('poloniex', 'hitbtc_sell')
    wallets_polo_hitbtc = coin_wallets('poloniex', 'hitbtc-poloniex')
    fc.parse_js(settings_polo_hitbtc, buysell_polo_hitbtc, wallets_polo_hitbtc)


run_fork()


    

