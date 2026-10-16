from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class MirReportRetrieveReqReportFormat(StrEnum):
    TRAMS = "TRAMS"
    CLIENTBASE = "CLIENTBASE"
    TRISEPT = "TRISEPT"
