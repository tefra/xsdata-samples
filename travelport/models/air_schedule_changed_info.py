from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_solution import AirPricingSolution

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirScheduleChangedInfo:
    """
    Returned when the requested schedule does not match the host system schedule
    Contents will be a new AirPricingSolution that contains all the new schedule
    information as well as the pricing information.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: None | AirPricingSolution = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        },
    )
