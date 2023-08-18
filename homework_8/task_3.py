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

    @classmethod             
    def eth_byn(cls):
        price_eth = cls.ETH * cls.USDT
        print(f'Текущий курс ETH в рублях составляет {price_eth} BYN')

Crypto.eth_byn()


Crypto.bit_byn()


print(Crypto.ETH)
