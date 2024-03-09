from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_create_reservation_req import (
    RailCreateReservationReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailCreateReservationPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailCreateReservationPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        rail_create_reservation_req: None | RailCreateReservationReq = field(
            default=None,
            metadata={
                "name": "RailCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
