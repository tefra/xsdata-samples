from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareDiscount(Enum):
    """
    Fare Discount Calculation Method.
    """

    BASE_RE_CALC_USTAXES = "BaseReCalcUSTaxes"
    BASE_NO_RE_CALC_USTAXES = "BaseNoReCalcUSTaxes"
    BASE_TAX = "BaseTax"
