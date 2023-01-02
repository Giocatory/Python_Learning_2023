crypto_valet = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "XRP": "Ripple"
}
print(crypto_valet["BTC"])  # Bitcoin
print(crypto_valet)  # {'BTC': 'Bitcoin', 'ETH': 'Ethereum', 'XRP': 'Ripple'}

# add element
crypto_valet["XMR"] = "Monero"
crypto_valet["ADA"] = "Cortana"
print(crypto_valet)  # {'BTC': 'Bitcoin', 'ETH': 'Ethereum', 'XRP': 'Ripple', 'XMR': 'Monero', 'ADA': 'Cortana'}

# delete element
del crypto_valet["ADA"]
print(crypto_valet)  # {'BTC': 'Bitcoin', 'ETH': 'Ethereum', 'XRP': 'Ripple', 'XMR': 'Monero'

# "in" dict
print("BTC" in crypto_valet)  # True
print("ETH" in crypto_valet.keys())  # True
print("ETH" in crypto_valet.items())  # False
print("Monero" in crypto_valet.values())  # True
