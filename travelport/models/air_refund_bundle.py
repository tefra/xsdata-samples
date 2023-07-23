from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_refund_bundle_refund_type import AirRefundBundleRefundType
from travelport.models.air_refund_info import AirRefundInfo
from travelport.models.name_1 import Name1
from travelport.models.tax_info import TaxInfo
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRefundBundle:
    """
    Bundle refund, pricing, and penalty information for one ticket number Used both
    in request and response.

    Parameters
    ----------
    air_refund_info
    name
    tax_info
    waiver_code
    ticket_number
    ptc
        Specifies the passenger type code for 1P
    refund_type
        Specifies whether this bundle was auto or manually generated
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_info: None | AirRefundInfo = field(
        default=None,
        metadata={
            "name": "AirRefundInfo",
            "type": "Element",
            "required": True,
        }
    )
    name: list[Name1] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )
    ptc: None | object = field(
        default=None,
        metadata={
            "name": "PTC",
            "type": "Attribute",
        }
    )
    refund_type: None | AirRefundBundleRefundType = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Attribute",
        }
    )
