class Assets(dict):
    def __init__(self):
        coins = {'AE': 'aeternity',
                 'ANT': 'aragon',
                 'BAT': 'basic-attention-token',
                 'BCH': 'bitcoin-cash',
                 'BLK': 'blackcoin',
                 'BNB': 'binance-coin',
                 'BNT': 'bancor',
                 'BSV': 'bitcoin-sv',
                 'BTC': 'bitcoin',
                 'BTG': 'bitcoin-gold',
                 'CLAM': 'clams',
                 'CVC': 'civic',
                 'DAI': 'dai',
                 'DASH': 'dash',
                 'DCR': 'decred',
                 'DGB': 'digibyte',
                 'DNT': 'district0x',
                 'DOGE': 'dogecoin',
                 'EDG': 'edgeless',
                 'ETC': 'ethereum-classic',
                 'ETH': 'ethereum',
                 'FCT': 'factom',
                 'FUN': 'funfair',
                 'GAME': 'gamecredits',
                 'GNO': 'gnosis-gno',
                 'GNT': 'golem-network-tokens',
                 'GRIN': 'grin',
                 'GUP': 'guppy',
                 'KMD': 'komodo',
                 'LBC': 'library-credit',
                 'LSK': 'lisk',
                 'LTC': 'litecoin',
                 'MAID': 'maidsafecoin',
                 'MANA': 'decentraland',
                 'MKR': 'maker',
                 'MONA': 'monacoin',
                 'MSC': 'omni',
                 'NEO': 'neo',
                 'NMC': 'namecoin',
                 'NMR': 'numeraire',
                 'NVC': 'novacoin',
                 'NXT': 'nxt',
                 'OMG': 'omisego',
                 'POLY': 'polymath-network',
                 'POT': 'potcoin',
                 'PPC': 'peercoin',
                 'QTUM': 'qtum',
                 'RCN': 'ripio-credit-network',
                 'RDD': 'reddcoin',
                 'REP': 'augur',
                 'RLC': 'rlc',
                 'SALT': 'salt',
                 'SC': 'siacoin',
                 'SNT': 'status',
                 'STEEM': 'steem',
                 'STORJ': 'storj',
                 'SWT': 'swarm-city',
                 'TUSD': 'trueusd',
                 'USDT': 'tether',
                 'VRC': 'vericoin',
                 'VTC': 'vertcoin',
                 'WAVES': 'waves',
                 'WINGS': 'wings',
                 'XEM': 'nem',
                 'XMR': 'monero',
                 'XRP': 'ripple',
                 'ZEC': 'zcash',
                 'ZIL': 'zilliqa',
                 'ZRX': '0x'}
        super().__init__(coins)

    @property
    def coins(self):
        return list(self.keys())

    @property
    def names(self):
        return list(self.values())
