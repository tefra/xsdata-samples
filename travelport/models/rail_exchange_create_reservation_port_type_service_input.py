from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_exchange_req import RailExchangeReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class RailExchangeCreateReservationPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | RailExchangeCreateReservationPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        rail_exchange_req: None | RailExchangeReq = field(
            default=None,
            metadata={
                "name": "RailExchangeReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/rail_v52_0",
            }
        )
