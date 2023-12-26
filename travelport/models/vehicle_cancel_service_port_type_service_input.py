from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.supported_versions import SupportedVersions
from travelport.models.vehicle_cancel_req import VehicleCancelReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleCancelServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | VehicleCancelServicePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | VehicleCancelServicePortTypeServiceInput.Body = field(
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
        vehicle_cancel_req: None | VehicleCancelReq = field(
            default=None,
            metadata={
                "name": "VehicleCancelReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
