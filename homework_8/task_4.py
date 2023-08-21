class MyMeta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.BTC = 27900  
        cls.ETH = 1700
        cls.USDT = 3


class Crypto(metaclass = MyMeta):
        
        @staticmethod        
        def bit_byn():
            price_btc = 27900 * 3
            print(f'Текущий курс BTC в рублях составляет {price_btc} BYN ')

        @classmethod             
        def eth_byn(cls):
            price_eth = cls.ETH * cls.USDT
            print(f'Текущий курс ETH в рублях составляет {price_eth} BYN')


res = Crypto()
print(res.eth_byn())