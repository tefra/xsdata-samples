from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.etr import Etr
from travelport.models.void_result_info import VoidResultInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirVoidDocumentRsp(BaseRsp1):
    """Result of void ticket request.

    Includes ticket number of voided tickets and air segments with
    updated status.

    Parameters
    ----------
    etr
        Provider: 1G,1V.
    void_result_info
        Provider: 1G,1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    etr: list[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    void_result_info: list[VoidResultInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidResultInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
