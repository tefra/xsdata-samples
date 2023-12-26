from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class PriceMatchError:
    """
    Parameters
    ----------
    error_message
    vendor_code
        The code of the vendor (e.g.  HZ, etc.)
    hotel_chain
        2 Letter Hotel Chain Code
    hotel_code
        Unique hotel identifier for the channel.
    req_base
        BaseRate in the request.
    rsp_base
        BaseRate retruned from the supplier.
    base_diff
        BaseRate Difference.
    req_total
        Estimated Total Amount in the request.
    rsp_total
        Estimated Total Amount returned from the supplier.
    total_diff
        Estimated Total Amount difference.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/common_v52_0"

    error_message: None | str = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "required": True,
        },
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    hotel_chain: None | str = field(
        default=None,
        metadata={
            "name": "HotelChain",
            "type": "Attribute",
            "length": 2,
        },
    )
    hotel_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    req_base: None | Decimal = field(
        default=None,
        metadata={
            "name": "ReqBase",
            "type": "Attribute",
        },
    )
    rsp_base: None | Decimal = field(
        default=None,
        metadata={
            "name": "RspBase",
            "type": "Attribute",
        },
    )
    base_diff: None | Decimal = field(
        default=None,
        metadata={
            "name": "BaseDiff",
            "type": "Attribute",
        },
    )
    req_total: None | Decimal = field(
        default=None,
        metadata={
            "name": "ReqTotal",
            "type": "Attribute",
        },
    )
    rsp_total: None | Decimal = field(
        default=None,
        metadata={
            "name": "RspTotal",
            "type": "Attribute",
        },
    )
    total_diff: None | Decimal = field(
        default=None,
        metadata={
            "name": "TotalDiff",
            "type": "Attribute",
        },
    )
