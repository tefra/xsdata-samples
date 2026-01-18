from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.flight_time_table_req import FlightTimeTableReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class FlightTimeTablePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: FlightTimeTablePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        flight_time_table_req: FlightTimeTableReq = field(
            metadata={
                "name": "FlightTimeTableReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
