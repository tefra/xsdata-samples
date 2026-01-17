from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeCarrierCode(Enum):
    """
    Defines the type of booking codes (Primary or Secondary).
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
