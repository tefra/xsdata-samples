from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeUnitWeight(StrEnum):
    """
    The available units of weight.
    """

    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"
