from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.emdinfo import Emdinfo
from travelport.models.emdsummary_info import EmdsummaryInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdretrieveRsp(BaseRsp1):
    """
    Electronic Miscellaneous Document list and detail retrieve response.Supported
    providers are 1G/1V/1P.

    Parameters
    ----------
    emdinfo
        Provider: 1G/1V/1P.
    emdsummary_info
        Provider: 1G/1V/1P.
    """

    class Meta:
        name = "EMDRetrieveRsp"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdinfo: None | Emdinfo = field(
        default=None,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
        },
    )
    emdsummary_info: list[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
