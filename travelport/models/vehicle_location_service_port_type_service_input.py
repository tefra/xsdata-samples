from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_location_req import VehicleLocationReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class VehicleLocationServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: VehicleLocationServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        vehicle_location_req: VehicleLocationReq = field(
            metadata={
                "name": "VehicleLocationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
