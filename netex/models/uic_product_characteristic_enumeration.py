from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UicProductCharacteristicEnumeration(Enum):
    TARIFF_COMMUN_VOYAGEURS = "tariffCommunVoyageurs"
    ALL_INCLUSIVE_PRICE = "allInclusivePrice"
    EAST_WEST_TARIFF = "eastWestTariff"
    TRAIN_WITH_TCV_AND_MARKET_PRICE = "trainWithTcvAndMarketPrice"
    NO_PUBLISHED_TARIFF = "noPublishedTariff"
