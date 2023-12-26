from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.mir_report_retrieve_req import MirReportRetrieveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ReportRetrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ReportRetrievePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mir_report_retrieve_req: None | MirReportRetrieveReq = field(
            default=None,
            metadata={
                "name": "MirReportRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
