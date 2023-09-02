from dataclasses import dataclass


@dataclass
class Crypto:
    BTC: int = 27900  
    ETH: int = 1700
    USDT: int = 3

print(Crypto.ETH)
print(Crypto.BTC)
print(Crypto.USDT)