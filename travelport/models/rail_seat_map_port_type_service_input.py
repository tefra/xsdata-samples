from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_seat_map_req import RailSeatMapReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailSeatMapPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailSeatMapPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        rail_seat_map_req: None | RailSeatMapReq = field(
            default=None,
            metadata={
                "name": "RailSeatMapReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            },
        )
