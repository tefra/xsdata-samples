from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UicProductCharacteristicEnumeration(StrEnum):
    TARIFF_COMMUN_VOYAGEURS = "tariffCommunVoyageurs"
    ALL_INCLUSIVE_PRICE = "allInclusivePrice"
    EAST_WEST_TARIFF = "eastWestTariff"
    TRAIN_WITH_TCV_AND_MARKET_PRICE = "trainWithTcvAndMarketPrice"
    NO_PUBLISHED_TARIFF = "noPublishedTariff"
