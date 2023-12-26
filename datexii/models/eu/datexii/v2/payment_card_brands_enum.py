from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PaymentCardBrandsEnum(Enum):
    """
    Brands of payment cards.

    :cvar AMERICAN_EXPRESS: American Express
    :cvar CIRRUS: Cirrus
    :cvar DINERS_CLUB: Diners Club
    :cvar DISCOVER_CARD: Discover Card
    :cvar GIRO_CARD: Girocard
    :cvar MAESTRO: Maestro
    :cvar MASTER_CARD: MasterCard
    :cvar VISA: Visa
    :cvar V_PAY: V PAY
    :cvar OTHER: Other
    """

    AMERICAN_EXPRESS = "americanExpress"
    CIRRUS = "cirrus"
    DINERS_CLUB = "dinersClub"
    DISCOVER_CARD = "discoverCard"
    GIRO_CARD = "giroCard"
    MAESTRO = "maestro"
    MASTER_CARD = "masterCard"
    VISA = "visa"
    V_PAY = "vPay"
    OTHER = "other"
