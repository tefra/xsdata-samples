from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_reservation_display_details_req import (
    ProviderReservationDisplayDetailsReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProviderReservationDisplayServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProviderReservationDisplayServicePortTypeServiceInput.Body = (
        field(
            default=None,
            metadata={
                "name": "Body",
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        provider_reservation_display_details_req: (
            None | ProviderReservationDisplayDetailsReq
        ) = field(
            default=None,
            metadata={
                "name": "ProviderReservationDisplayDetailsReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
