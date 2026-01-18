from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_merchandising_offer_availability_req import (
    AirMerchandisingOfferAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class AirMerchandisingOfferAvailabilityPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AirMerchandisingOfferAvailabilityPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        air_merchandising_offer_availability_req: AirMerchandisingOfferAvailabilityReq = field(
            metadata={
                "name": "AirMerchandisingOfferAvailabilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
