from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.schedule_search_req import ScheduleSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirScheduleSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirScheduleSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        schedule_search_req: None | ScheduleSearchReq = field(
            default=None,
            metadata={
                "name": "ScheduleSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
