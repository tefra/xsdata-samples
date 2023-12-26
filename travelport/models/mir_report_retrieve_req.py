from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.mir_report_retrieve_req_report_format import (
    MirReportRetrieveReqReportFormat,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MirReportRetrieveReq(BaseReq1):
    """
    Retrieve a report.

    Parameters
    ----------
    locator_code
        The locator code of the PNR that the MIR is created for.
    report_format
        MIR report format type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 8,
        },
    )
    report_format: None | MirReportRetrieveReqReportFormat = field(
        default=None,
        metadata={
            "name": "ReportFormat",
            "type": "Attribute",
        },
    )
