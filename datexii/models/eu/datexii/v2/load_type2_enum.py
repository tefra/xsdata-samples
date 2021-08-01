from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LoadType2Enum(Enum):
    """
    Loads that are currently not supported in loadType.

    :cvar REFRIGERATED_GOODS: Refrigerated goods.
    """
    REFRIGERATED_GOODS = "refrigeratedGoods"
