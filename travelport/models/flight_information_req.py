from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.flight_info_criteria import FlightInfoCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightInformationReq(BaseReq1):
    """
    Request for the Flight Info of segments.

    Parameters
    ----------
    flight_info_criteria
        Provider: 1G,1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_info_criteria: list[FlightInfoCriteria] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoCriteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
