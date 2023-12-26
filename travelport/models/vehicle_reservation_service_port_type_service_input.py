from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.supported_versions import SupportedVersions
from travelport.models.vehicle_create_reservation_req import (
    VehicleCreateReservationReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleReservationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | VehicleReservationServicePortTypeServiceInput.Header = (
        field(
            default=None,
            metadata={
                "name": "Header",
                "type": "Element",
            },
        )
    )
    body: None | VehicleReservationServicePortTypeServiceInput.Body = field(
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
        vehicle_create_reservation_req: None | VehicleCreateReservationReq = field(
            default=None,
            metadata={
                "name": "VehicleCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
