from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_refund_bundle import AirRefundBundle
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.tcrrefund_bundle import TcrrefundBundle

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirRefundQuoteRsp(BaseRsp1):
    """
    Parameters
    ----------
    air_refund_bundle
    tcrrefund_bundle
        Provider: ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_bundle: list[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tcrrefund_bundle: list[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        },
    )
