from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_refund_info import AirRefundInfo
from travelport.models.air_segment import AirSegment
from travelport.models.fee_info import FeeInfo
from travelport.models.host_token_1 import HostToken1
from travelport.models.tax_info import TaxInfo
from travelport.models.tcrrefund_bundle_refund_type import (
    TcrrefundBundleRefundType,
)
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TcrrefundBundle:
    """
    Bundle refund, pricing, and penalty information for a TCR reservation Used both
    in request and response.

    Parameters
    ----------
    air_refund_info
    waiver_code
    air_segment
    fee_info
    tax_info
        Itinerary level taxes
    host_token
    tcrnumber
        The identifying number for a Ticketless Air Reservation.
    refund_type
        Specifies whether this bundle was auto or manually generated
    refund_access_code
    """

    class Meta:
        name = "TCRRefundBundle"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_info: None | AirRefundInfo = field(
        default=None,
        metadata={
            "name": "AirRefundInfo",
            "type": "Element",
            "required": True,
        },
    )
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tcrnumber: None | str = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    refund_type: None | TcrrefundBundleRefundType = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Attribute",
            "required": True,
        },
    )
    refund_access_code: None | str = field(
        default=None,
        metadata={
            "name": "RefundAccessCode",
            "type": "Attribute",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_length": 1,
            "max_length": 32,
        },
    )
