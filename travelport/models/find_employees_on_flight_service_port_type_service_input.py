from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.find_employees_on_flight_req import (
    FindEmployeesOnFlightReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class FindEmployeesOnFlightServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: FindEmployeesOnFlightServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        find_employees_on_flight_req: FindEmployeesOnFlightReq = field(
            metadata={
                "name": "FindEmployeesOnFlightReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
