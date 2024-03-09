from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class TypePnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """

    FORM_OF_PAYMENT = "FormOfPayment"
    OSI = "OSI"
    ACCOUNTING_REMARK = "AccountingRemark"
    GENERAL_REMARK = "GeneralRemark"
    UNASSOCIATED_REMARK = "UnassociatedRemark"
