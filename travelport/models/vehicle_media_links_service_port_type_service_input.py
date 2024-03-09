from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_media_links_req import VehicleMediaLinksReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleMediaLinksServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleMediaLinksServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        vehicle_media_links_req: None | VehicleMediaLinksReq = field(
            default=None,
            metadata={
                "name": "VehicleMediaLinksReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            },
        )
