from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.supported_versions import SupportedVersions
from travelport.models.vehicle_create_reservation_req import (
    VehicleCreateReservationReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class VehicleReservationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: VehicleReservationServicePortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: VehicleReservationServicePortTypeServiceInput.Body = field(
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
        vehicle_create_reservation_req: VehicleCreateReservationReq = field(
            metadata={
                "name": "VehicleCreateReservationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
