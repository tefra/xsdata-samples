from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CurrencyEnum(Enum):
    """
    Three letter code defining the currency according to ISO 4217 (e.g.

    EUR for Euro). This enumeration only contains European currencies
    including the US dollar.

    :cvar EUR: Euro
    :cvar ALL: Lek (Albania)
    :cvar AMD: Armeniam Dram
    :cvar AZN: Azerbaijanian Manat
    :cvar BAM: Convertible Mark (Bosnia and Herzogowina)
    :cvar BGN: Bulgarian Lev
    :cvar BYR: Belarussian Ruble
    :cvar CHF: Swiss Franc
    :cvar CZK: Czech Koruna
    :cvar DKK: Danish Krone
    :cvar GBP: Pound Sterling
    :cvar GEL: Lari (Georgia)
    :cvar HRK: Croatian Kuna
    :cvar HUF: Forint (Hungary)
    :cvar ISK: Iceland Krona
    :cvar LTL: Litas (Lithuania)
    :cvar MDL: Moldovan Leu
    :cvar MKD: Denar
    :cvar NOK: Norwegian Krone
    :cvar PLN: Zloty
    :cvar RON: New Romanian Leu
    :cvar RSD: Serbian Dinar
    :cvar RUB: Russian Ruble
    :cvar SEK: Swedish Krona
    :cvar TRY: Turkish Lira
    :cvar UAH: Hryvnia (Ukraine)
    :cvar USD: US Dollar
    :cvar OTHER: Another currency.
    """

    EUR = "eur"
    ALL = "all"
    AMD = "amd"
    AZN = "azn"
    BAM = "bam"
    BGN = "bgn"
    BYR = "byr"
    CHF = "chf"
    CZK = "czk"
    DKK = "dkk"
    GBP = "gbp"
    GEL = "gel"
    HRK = "hrk"
    HUF = "huf"
    ISK = "isk"
    LTL = "ltl"
    MDL = "mdl"
    MKD = "mkd"
    NOK = "nok"
    PLN = "pln"
    RON = "ron"
    RSD = "rsd"
    RUB = "rub"
    SEK = "sek"
    TRY = "try"
    UAH = "uah"
    USD = "usd"
    OTHER = "other"
