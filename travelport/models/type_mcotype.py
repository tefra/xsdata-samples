from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeMcotype(Enum):
    """
    The available types for an MCO.
    """

    AGENCY_SERVICE_FEE = "AgencyServiceFee"
    EXCHANGE_RESIDUAL = "ExchangeResidual"
    AIRLINE_SERVICE_FEE = "AirlineServiceFee"
