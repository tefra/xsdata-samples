from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_retrieve_req import VehicleRetrieveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class VehicleRetrieveServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: VehicleRetrieveServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        vehicle_retrieve_req: VehicleRetrieveReq = field(
            metadata={
                "name": "VehicleRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
