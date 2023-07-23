from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.vehicle_location_req import VehicleLocationReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleLocationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleLocationServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        vehicle_location_req: None | VehicleLocationReq = field(
            default=None,
            metadata={
                "name": "VehicleLocationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
