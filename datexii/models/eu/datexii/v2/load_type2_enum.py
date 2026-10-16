from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LoadType2Enum(StrEnum):
    """
    Loads that are currently not supported in loadType.

    :cvar REFRIGERATED_GOODS: Refrigerated goods.
    """

    REFRIGERATED_GOODS = "refrigeratedGoods"
