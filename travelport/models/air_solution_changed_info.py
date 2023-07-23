from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.air_solution_changed_info_reason_code import AirSolutionChangedInfoReasonCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider.

    If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were
    returned from the provider. If RetainReservation is Price, Schedule,
    or Both and there isn’t a price/schedule change, this element will
    not be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: None | AirPricingSolution = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: None | AirSolutionChangedInfoReasonCode = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
