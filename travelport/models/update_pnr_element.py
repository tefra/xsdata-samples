from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.action_status_1 import ActionStatus1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.osi_1 import Osi1
from travelport.models.unassociated_remark_1 import UnassociatedRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class UpdatePnrElement:
    """
    Container for PNR elements to be updated.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    action_status: None | ActionStatus1 = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    osi: list[Osi1] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    accounting_remark: list[AccountingRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    unassociated_remark: list[UnassociatedRemark1] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
