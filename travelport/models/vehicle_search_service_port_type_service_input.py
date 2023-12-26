from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.vehicle_search_availability_req import (
    VehicleSearchAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleSearchServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        vehicle_search_availability_req: None | VehicleSearchAvailabilityReq = field(
            default=None,
            metadata={
                "name": "VehicleSearchAvailabilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            },
        )
