from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.emdinfo import Emdinfo
from travelport.models.emdsummary_info import EmdsummaryInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdissuanceRsp(BaseRsp1):
    """
    Electronic Miscellaneous Document issuance response.Supported providers are
    1V/1G/1P.

    Parameters
    ----------
    emdsummary_info
        List of EMDSummaryInfo elements to show minimal information in
        issuance response. Appears for ShowDetails=false in the request.This
        is the default behaviour.
    emdinfo
        List of EMDInfo elements to show detailoed information in issuance
        response. Appears for ShowDetails=true in the request.
    """
    class Meta:
        name = "EMDIssuanceRsp"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdsummary_info: list[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emdinfo: list[Emdinfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
