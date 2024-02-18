from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_base_req import AirBaseReq
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.air_reservation_locator_code import (
    AirReservationLocatorCode,
)
from travelport.models.type_fare_rule_type import TypeFareRuleType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRepriceReq(AirBaseReq):
    """
    Request to reprice a solution.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
        },
    )
    air_pricing_solution: None | AirPricingSolution = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        },
    )
    ignore_availability: bool = field(
        default=False,
        metadata={
            "name": "IgnoreAvailability",
            "type": "Attribute",
        },
    )
