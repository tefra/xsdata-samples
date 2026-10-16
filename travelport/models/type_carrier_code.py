from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeCarrierCode(StrEnum):
    """
    Defines the type of booking codes (Primary or Secondary).
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
