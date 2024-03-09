from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_availability_search_req import (
    RailAvailabilitySearchReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailAvailabilitySearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailAvailabilitySearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        rail_availability_search_req: None | RailAvailabilitySearchReq = field(
            default=None,
            metadata={
                "name": "RailAvailabilitySearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            },
        )
