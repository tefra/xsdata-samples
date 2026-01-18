from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_reservation_divide_req import (
    ProviderReservationDivideReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProviderReservationDivideServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProviderReservationDivideServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        provider_reservation_divide_req: ProviderReservationDivideReq = field(
            metadata={
                "name": "ProviderReservationDivideReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
