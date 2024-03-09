from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_create_reservation_req import (
    HotelCreateReservationReq,
)
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class HotelReservationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | HotelReservationServicePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | HotelReservationServicePortTypeServiceInput.Body = field(
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
        hotel_create_reservation_req: None | HotelCreateReservationReq = field(
            default=None,
            metadata={
                "name": "HotelCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
