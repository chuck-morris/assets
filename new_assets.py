import coins as c


class NewAssets(dict):

    def __init__(self):

        self.coins = {'2GIVE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ABY': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ADA': {'exchanges': ['binance', 'bittrex', 'kraken'], 'id': 'cardano', 'name': 'Cardano'},
                 'ADT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ADX': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'AE': {'exchanges': ['binance', 'felix'], 'id': 'aeternity', 'name': 'Aeternity'},
                 'AEON': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'AERGO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'AGI': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'AID': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'AION': {'exchanges': ['binance', 'bitfinex'], 'id': 'aion', 'name': 'Aion'},
                 'AMB': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'AMP': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ANKR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ANT': {'exchanges': ['bitfinex', 'bittrex', 'felix'], 'id': None, 'name': None},
                 'APPC': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'ARDR': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': 'ardor', 'name': 'Ardor'},
                 'ARK': {'exchanges': ['binance', 'bittrex'], 'id': 'ark', 'name': 'Ark'},
                 'ARN': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'ART': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'AST': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'ATMI': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'ATOM': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'AUC': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'AVT': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'BAT': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'basic-attention-token', 'name': 'Basic Attention Token'},
                 'BAY': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BCC': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'BCD': {'exchanges': ['binance'], 'id': 'bitcoin-diamond', 'name': 'Bitcoin Diamond'},
                 'BCH': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'bitcoin-cash', 'name': 'Bitcoin Cash'},
                 'BCI': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'BCN': {'exchanges': ['binance', 'poloniex'], 'id': 'bytecoin-bcn', 'name': 'Bytecoin'},
                 'BCPT': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'BFT': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'BITB': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BKX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BLK': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'BLOCK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BLT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BLZ': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'BNB': {'exchanges': ['binance', 'felix'], 'id': 'binance-coin', 'name': 'Binance Coin'},
                 'BNT': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'bancor', 'name': 'Bancor'},
                 'BORA': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BOXX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BQX': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'BRD': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'BRK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BRX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BSD': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BSV': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'bitcoin-sv', 'name': 'Bitcoin SV'},
                 'BTG': {'exchanges': ['binance', 'bitfinex', 'felix'], 'id': 'bitcoin-gold', 'name': 'Bitcoin Gold'},
                 'BTM': {'exchanges': ['bittrex'], 'id': 'bytom', 'name': 'Bytom'},
                 'BTS': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': 'bitshares', 'name': 'BitShares'},
                 'BTT': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'BTU': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'BURST': {'exchanges': ['bittrex', 'poloniex'], 'id': None, 'name': None},
                 'CANN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CBC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CBT': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'CDT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'CELR': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'CHAT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'CLAM': {'exchanges': ['poloniex', 'felix'], 'id': None, 'name': None},
                 'CLO': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'CLOAK': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'CMCT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CMT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'CND': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'COVAL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CRO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CRW': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CTXC': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'CURE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'CVC': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'DADI': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'DAI': {'exchanges': ['bitfinex', 'felix'], 'id': 'dai', 'name': 'Dai'},
                 'DASH': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'dash', 'name': 'Dash'},
                 'DATA': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'DCR': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': 'decred', 'name': 'Decred'},
                 'DCT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DENT': {'exchanges': ['binance', 'bittrex'], 'id': 'dent', 'name': 'Dent'},
                 'DGB': {'exchanges': ['bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'digibyte', 'name': 'DigiByte'},
                 'DGD': {'exchanges': ['binance'], 'id': 'digixdao', 'name': 'DigixDAO'},
                 'DLT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'DMD': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DMT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DNT': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': None, 'name': None},
                 'DOCK': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'DOGE': {'exchanges': ['bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'dogecoin', 'name': 'Dogecoin'}, 'DOPE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DRGN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DTA': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'DTB': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'DTH': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'DYN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'EBST': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'EDG': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'EDO': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'EDR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'EGC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ELF': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': 'aelf', 'name': 'aelf'},
                 'EMC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'EMC2': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ENG': {'exchanges': ['binance', 'bittrex'], 'id': 'enigma-project', 'name': 'Enigma'},
                 'ENJ': {'exchanges': ['binance', 'bittrex'], 'id': 'enjin-coin', 'name': 'Enjin Coin'},
                 'EOS': {'exchanges': ['binance', 'bitfinex', 'poloniex', 'kraken'], 'id': 'eos', 'name': 'EOS'},
                 'ESS': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'ETC': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'ethereum-classic', 'name': 'Ethereum Classic'},
                 'ETH': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'ethereum', 'name': 'Ethereum'},
                 'ETP': {'exchanges': ['bitfinex'], 'id': 'metaverse', 'name': 'Metaverse ETP'},
                 'EVX': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'EXCL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'EXP': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'FCT': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': 'factom', 'name': 'Factom'},
                 'FET': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'FLDC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'FLO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'FOAM': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'FSN': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'FTC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'FUEL': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'FUN': {'exchanges': ['binance', 'bitfinex', 'felix'], 'id': None, 'name': None},
                 'GAM': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GAME': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'GAS': {'exchanges': ['binance', 'poloniex'], 'id': None, 'name': None},
                 'GBG': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GBYTE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GEO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GLC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GNO': {'exchanges': ['bittrex', 'kraken', 'felix'], 'id': None, 'name': None},
                 'GNT': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'golem-network-tokens', 'name': 'Golem'},
                 'GO': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'GOLOS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GRC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'GRIN': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'GRS': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'GTO': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'GUP': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'GVT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'GXS': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'HC': {'exchanges': ['binance'], 'id': 'hypercash', 'name': 'HyperCash'},
                 'HMQ': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'HOT': {'exchanges': ['binance'], 'id': 'holo', 'name': 'Holo'},
                 'HSR': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'HST': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'HUC': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'HXRO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'HYDRO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'Hydro Protocol': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'ICN': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'ICX': {'exchanges': ['binance'], 'id': 'icon', 'name': 'ICON'},
                 'IGNIS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'IHT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'INCNT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'INS': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'IOC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ION': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'IOP': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'IOST': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': 'iostoken', 'name': 'IOST'},
                 'IOTA': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'IOTX': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'IQ': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'JNT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'KEY': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'KMD': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': 'komodo', 'name': 'Komodo'},
                 'KNC': {'exchanges': ['binance', 'bitfinex', 'poloniex'], 'id': 'kyber-network', 'name': 'Kyber Network'}, 'KORE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'LBA': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'LBC': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'LEND': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'LINK': {'exchanges': ['binance'], 'id': 'chainlink', 'name': 'Chainlink'},
                 'LOOM': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': 'loom-network', 'name': 'Loom Network'}, 'LPT': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'LRC': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': 'loopring', 'name': 'Loopring'},
                 'LSK': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': 'lisk', 'name': 'Lisk'},
                 'LTC': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'litecoin', 'name': 'Litecoin'},
                 'LUN': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'LYM': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'MAID': {'exchanges': ['poloniex', 'felix'], 'id': 'maidsafecoin', 'name': 'MaidSafeCoin'},
                 'MANA': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'decentraland', 'name': 'Decentraland'},
                 'MCO': {'exchanges': ['binance', 'bittrex'], 'id': 'crypto-com', 'name': 'Crypto.com'},
                 'MDA': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'MEDX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MEME': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MER': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MET': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'META': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MFT': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'MITH': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'MKR': {'exchanges': ['bitfinex', 'felix'], 'id': 'maker', 'name': 'Maker'},
                 'MLN': {'exchanges': ['bittrex', 'kraken'], 'id': None, 'name': None},
                 'MOBI': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MOC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MOD': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'MONA': {'exchanges': ['bittrex', 'felix'], 'id': 'monacoin', 'name': 'MonaCoin'},
                 'MORE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MTH': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'MTL': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'MTN': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'MUE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'MUSIC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NANO': {'exchanges': ['binance'], 'id': 'nano', 'name': 'Nano'},
                 'NAS': {'exchanges': ['binance'], 'id': 'nebulas-token', 'name': 'Nebulas'},
                 'NAV': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': None, 'name': None},
                 'NBT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NCASH': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'NEBL': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'NEO': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'felix'], 'id': 'neo', 'name': 'NEO'},
                 'NEOS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NGC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NKN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NLC2': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NLG': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NMC': {'exchanges': ['poloniex', 'felix'], 'id': None, 'name': None},
                 'NMR': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'NPXS': {'exchanges': ['binance', 'bittrex'], 'id': 'pundi-x', 'name': 'Pundi X'},
                 'NULS': {'exchanges': ['binance'], 'id': 'nuls', 'name': 'NULS'},
                 'NXC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'NXS': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'NXT': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'OAX': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'OCN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ODE': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'OK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'OMG': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'omisego', 'name': 'OmiseGO'}, 'OMN': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'OMNI': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'ONG': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'ONT': {'exchanges': ['binance', 'bittrex'], 'id': 'ontology', 'name': 'Ontology'},
                 'ORBS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ORS Group': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'OST': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'PAI': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'PAL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PART': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PASC': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'PAX': {'exchanges': ['binance', 'bittrex'], 'id': 'paxos-standard-token', 'name': 'Paxos Standard Token'},
                 'PAY': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PHX': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'PI': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PINK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PIVX': {'exchanges': ['binance', 'bittrex'], 'id': 'pivx', 'name': 'PIVX'},
                 'PLA': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PMA': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'POA': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'POE': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'POLY': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'polymath-network', 'name': 'Polymath'},
                 'POT': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'POWR': {'exchanges': ['binance', 'bittrex'], 'id': 'power-ledger', 'name': 'Power Ledger'},
                 'PPC': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'PPT': {'exchanges': ['binance'], 'id': 'populous', 'name': 'Populous'},
                 'PRO': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PTON': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'PTOY': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'QASH': {'exchanges': ['bitfinex'], 'id': 'qash', 'name': 'QASH'},
                 'QKC': {'exchanges': ['binance'], 'id': 'quarkchain', 'name': 'QuarkChain'},
                 'QLC': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'QNT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'QRL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'QSP': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'QTUM': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'qtum', 'name': 'Qtum'},
                 'QWARK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'RADS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'RBT': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'RCN': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'felix'], 'id': None, 'name': None},
                 'RDD': {'exchanges': ['bittrex', 'felix'], 'id': 'reddcoin', 'name': 'ReddCoin'},
                 'RDN': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'REN': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'REP': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'augur', 'name': 'Augur'},
                 'REQ': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'RFR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'RIF': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'RLC': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'felix'], 'id': 'rlc', 'name': 'iExec RLC'},
                 'RPX': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'RRT': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'RVN': {'exchanges': ['binance', 'bittrex'], 'id': 'ravencoin', 'name': 'Ravencoin'},
                 'RVR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SALT': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': None, 'name': None},
                 'SAN': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'SBD': {'exchanges': ['bittrex', 'poloniex'], 'id': None, 'name': None},
                 'SC': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': 'siacoin', 'name': 'Siacoin'},
                 'SEER': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'SEN': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'SEQ': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SERV': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SHIFT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SIB': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SKY': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'SLR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SLS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SLT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SNGLS': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'SNM': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'SNT': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': 'status', 'name': 'Status'}, 'SOLVE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SPANK': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'SPC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SPHR': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SPND': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SRN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'STEEM': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': 'steem', 'name': 'Steem'},
                 'STORJ': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'STORM': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'STRAT': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': 'stratis', 'name': 'Stratis'},
                 'SUB': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'SWIFT': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SWT': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'SYNX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'SYS': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': None, 'name': None},
                 'THC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'THETA': {'exchanges': ['binance'], 'id': 'theta-token', 'name': 'Theta Token'},
                 'TIX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'TKS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'TNB': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'TNT': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'TRAC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'TRIG': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'TRX': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': 'tron', 'name': 'TRON'},
                 'TTC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'TUBE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'TUSD': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': 'trueusd', 'name': 'TrueUSD'},
                 'TX': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'UBQ': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'UKG': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'UP': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'UPP': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'USDC': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'USDS': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'UTK': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'VBK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'VEE': {'exchanges': ['bitfinex', 'bittrex'], 'id': None, 'name': None},
                 'VEN': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'VET': {'exchanges': ['binance', 'bitfinex'], 'id': 'vechain', 'name': 'VeChain'},
                 'VIA': {'exchanges': ['binance', 'bittrex', 'poloniex'], 'id': None, 'name': None},
                 'VIB': {'exchanges': ['binance', 'bittrex'], 'id': None, 'name': None},
                 'VIBE': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'VITE': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'VRC': {'exchanges': ['bittrex', 'felix'], 'id': None, 'name': None},
                 'VRM': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'VSY': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'VTC': {'exchanges': ['bittrex', 'poloniex', 'felix'], 'id': None, 'name': None},
                 'WABI': {'exchanges': ['binance'], 'id': None, 'name': None},
                 'WAN': {'exchanges': ['binance'], 'id': 'wanchain', 'name': 'Wanchain'},
                 'WAVES': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': 'waves', 'name': 'Waves'},
                 'WAX': {'exchanges': ['bitfinex', 'bittrex'], 'id': 'wax', 'name': 'WAX'},
                 'WINGS': {'exchanges': ['binance', 'bittrex', 'felix'], 'id': None, 'name': None},
                 'WPR': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'WTC': {'exchanges': ['binance'], 'id': 'waltonchain', 'name': 'Waltonchain'},
                 'XCP': {'exchanges': ['bittrex', 'poloniex'], 'id': None, 'name': None},
                 'XDN': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XEL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XEM': {'exchanges': ['binance', 'bittrex', 'poloniex', 'felix'], 'id': 'nem', 'name': 'NEM'},
                 'XHV': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XLM': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken'], 'id': 'stellar', 'name': 'Stellar'},
                 'XMR': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'monero', 'name': 'Monero'},
                 'XMY': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XNK': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XPM': {'exchanges': ['poloniex'], 'id': None, 'name': None},
                 'XRP': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'ripple', 'name': 'XRP'},
                 'XST': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XTZ': {'exchanges': ['bitfinex', 'kraken'], 'id': 'tezos', 'name': 'Tezos'},
                 'XVG': {'exchanges': ['binance', 'bitfinex', 'bittrex'], 'id': 'verge', 'name': 'Verge'},
                 'XWC': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'XZC': {'exchanges': ['binance', 'bittrex'], 'id': 'zcoin', 'name': 'Zcoin'},
                 'YOYOW': {'exchanges': ['binance', 'bitfinex'], 'id': None, 'name': None},
                 'ZCL': {'exchanges': ['bittrex'], 'id': None, 'name': None},
                 'ZCN': {'exchanges': ['bitfinex'], 'id': None, 'name': None},
                 'ZEC': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'kraken', 'felix'], 'id': 'zcash', 'name': 'Zcash'},
                 'ZEN': {'exchanges': ['binance', 'bittrex'], 'id': 'zencash', 'name': 'Horizen'},
                 'ZIL': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'felix'], 'id': 'zilliqa', 'name': 'Zilliqa'},
                 'ZRX': {'exchanges': ['binance', 'bitfinex', 'bittrex', 'poloniex', 'felix'], 'id': '0x', 'name': '0x'}
                 }
        super(NewAssets, self).__init__()

    @property
    def symbols(self):
        return self.coins.keys()

    def exchanges(self, symbol):
        return self.coins[symbol]['exchanges']

    @property
    def felix(self):
        symbols = []
        for coin in self.coins:
            if 'felix' in self.coins[coin]['exchanges']:
                symbols.append(coin)
        return symbols

    def name(self, symbol):
        return self.coins[symbol]['name']

    def id(self, symbol):
        return self.coins[symbol]['id']

    def symbol(self, id):
        for coin in self.coins:
            if self.coins[coin]['id'] == id:
                return coin


#need to add bitcoin
#need to check on slugs for felix
#need to check felix asset count
assets = NewAssets()
print(assets.coins)
print(assets.symbols)
print(assets.exchanges('ZRX'))
print(assets.felix)
print(len(assets.felix))
print(assets.name('BTS'))
print(assets.id('MANA'))
print(assets.symbol('bancor'))





