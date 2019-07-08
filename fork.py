import func as fc
from static import Static
from component import Component
from wallet import coin_wallets


def run_fork():
    ### By in Bittrex Sell in Hitbtc###
    settings_bittrex_hitbtc = Static('bittrex-hitbtc')
    buysell_bittrex_hitbtc = Component('bittrex', 'hitbtc_sell')
    wallets_bittrex_hitbtc = coin_wallets('bittrex', 'hitbtc-bittrex')
    fc.parse_js(settings_bittrex_hitbtc, buysell_bittrex_hitbtc, wallets_bittrex_hitbtc)

    ### By in Hitbtc sell in Bittrex###
    settings_hitbtc_bittrex = Static('hitbtc-bittrex')
    buysell_hitbtc_bittrex = Component('hitbtc', 'bittrex_sell')
    wallets_hitbtc_bittrex = coin_wallets('hitbtc', 'hitbtc-bittrex')
    fc.parse_js(settings_hitbtc_bittrex, buysell_hitbtc_bittrex, wallets_hitbtc_bittrex)
    
    ### Buy in Bittrex sell in Binance##
    settings_bittrex_binance = Static('bittrex-binance')
    buysell_bittrex_binance = Component('bittrex', 'binance_sell')
    wallets_bittrex_binance = coin_wallets('bittrex', 'bittrex-binance')
    fc.parse_js(settings_bittrex_binance, buysell_bittrex_binance, wallets_bittrex_binance)

    ### Buy in Binance Sell in Bittrex
    settings_binance_bittrex = Static('binance-bittrex')
    buysell_binance_bittrex = Component('binance', 'bittrex_sell')
    wallets_binance_bittrex = coin_wallets('binance', 'bittrex-binance')
    fc.parse_js(settings_binance_bittrex, buysell_binance_bittrex, wallets_binance_bittrex)

    ### Buy in HitBtc Sell in Binance
    settings_hitbtc_binance =  Static('hitbtc-binance')
    buysell_hitbtc_binance = Component('hitbtc', 'binance_sell')
    wallets_hitbtc_binance = coin_wallets('hitbtc', 'hitbtc-binance')
    fc.parse_js(settings_hitbtc_binance, buysell_hitbtc_binance, wallets_hitbtc_binance)

    ### Buy in Binance Sell in Hitbtc
    settings_binance_hitbtc = Static('binance-hitbtc')
    buysell_binance_hitbtc = Component('binance', 'hitbtc_sell')
    wallets_binance_hitbtc = coin_wallets('binance', 'hitbtc-binance')
    fc.parse_js(settings_binance_hitbtc, buysell_binance_hitbtc, wallets_binance_hitbtc)









run_fork()


    

