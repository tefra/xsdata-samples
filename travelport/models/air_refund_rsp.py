from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.etr import Etr
from travelport.models.tcr import Tcr
from travelport.models.type_ticket_failure_info import TypeTicketFailureInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirRefundRsp(BaseRsp1):
    """
    Parameters
    ----------
    etr
        Provider: ACH.
    tcr
        Provider: ACH.
    refund_failure_info
        Provider: ACH.
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
    tcr: list[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    refund_failure_info: list[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "RefundFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
