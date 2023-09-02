from dataclasses import dataclass


@dataclass
class Crypto:
    BTC: int = 27900  
    ETH: int = 1700
    USDT: int = 3


    @staticmethod        
    def bit_byn():
        price_btc = 27900 * 3
        print(f'Текущий курс BTC в рублях составляет {price_btc} BYN ')

Crypto.bit_byn()