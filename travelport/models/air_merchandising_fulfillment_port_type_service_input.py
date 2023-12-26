from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_merchandising_fulfillment_req import (
    AirMerchandisingFulfillmentReq,
)
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirMerchandisingFulfillmentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | AirMerchandisingFulfillmentPortTypeServiceInput.Header = (
        field(
            default=None,
            metadata={
                "name": "Header",
                "type": "Element",
            },
        )
    )
    body: None | AirMerchandisingFulfillmentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        supported_versions: None | SupportedVersions = field(
            default=None,
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )

    @dataclass
    class Body:
        air_merchandising_fulfillment_req: None | AirMerchandisingFulfillmentReq = field(
            default=None,
            metadata={
                "name": "AirMerchandisingFulfillmentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
