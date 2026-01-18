from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_create_reservation_req import (
    RailCreateReservationReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class RailCreateReservationPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: RailCreateReservationPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        rail_create_reservation_req: RailCreateReservationReq = field(
            metadata={
                "name": "RailCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
