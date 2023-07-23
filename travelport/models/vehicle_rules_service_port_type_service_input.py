from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.vehicle_rules_req import VehicleRulesReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleRulesServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleRulesServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        vehicle_rules_req: None | VehicleRulesReq = field(
            default=None,
            metadata={
                "name": "VehicleRulesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            }
        )
