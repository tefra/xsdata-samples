from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class MirReportRetrieveRsp(BaseRsp1):
    """
    Carries the report payload.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    report: str = field(
        metadata={
            "name": "Report",
            "type": "Element",
            "required": True,
        }
    )
