from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.find_employees_on_flight_req import FindEmployeesOnFlightReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class FindEmployeesOnFlightServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | FindEmployeesOnFlightServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        find_employees_on_flight_req: None | FindEmployeesOnFlightReq = field(
            default=None,
            metadata={
                "name": "FindEmployeesOnFlightReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
