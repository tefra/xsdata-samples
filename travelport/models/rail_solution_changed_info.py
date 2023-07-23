from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.rail_solution_changed_info_reason_code import RailSolutionChangedInfoReasonCode

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider.

    If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were
    returned from the provider.  If RetainReservation is Price,
    Schedule, or Both and there isn’t a price/schedule change, this
    element will not be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_pricing_solution: None | RailPricingSolution = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: None | RailSolutionChangedInfoReasonCode = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
