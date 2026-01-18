from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.hotel_create_reservation_req import (
    HotelCreateReservationReq,
)
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelReservationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: HotelReservationServicePortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: HotelReservationServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Header:
        supported_versions: SupportedVersions = field(
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        hotel_create_reservation_req: HotelCreateReservationReq = field(
            metadata={
                "name": "HotelCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
