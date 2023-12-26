from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.continuity_check_override_1 import (
    ContinuityCheckOverride1,
)
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.rail_refund_req_refund_option import (
    RailRefundReqRefundOption,
)

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailRefundReq(BaseReq1):
    """
    Request to cancel the booking.

    Parameters
    ----------
    continuity_check_override
        This element will be used if user wants to override segment
        continuity check.
    form_of_payment
    locator_code
        The unique identifier for this rail reservation
    refund_option
        Customers choice to select the refund amount or retain as EVoucher
        for future use.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    continuity_check_override: None | ContinuityCheckOverride1 = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    refund_option: None | RailRefundReqRefundOption = field(
        default=None,
        metadata={
            "name": "RefundOption",
            "type": "Attribute",
        },
    )
