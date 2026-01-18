from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_upsell_search_availability_req import (
    VehicleUpsellSearchAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class VehicleUpsellSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: VehicleUpsellSearchServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        vehicle_upsell_search_availability_req: VehicleUpsellSearchAvailabilityReq = field(
            metadata={
                "name": "VehicleUpsellSearchAvailabilityReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
