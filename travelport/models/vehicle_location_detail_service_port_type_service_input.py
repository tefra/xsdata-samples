from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.session_context import SessionContext
from travelport.models.vehicle_location_detail_req import (
    VehicleLocationDetailReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleLocationDetailServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | VehicleLocationDetailServicePortTypeServiceInput.Header = (
        field(
            default=None,
            metadata={
                "name": "Header",
                "type": "Element",
            },
        )
    )
    body: None | VehicleLocationDetailServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            },
        )

    @dataclass
    class Body:
        vehicle_location_detail_req: None | VehicleLocationDetailReq = field(
            default=None,
            metadata={
                "name": "VehicleLocationDetailReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            },
        )
