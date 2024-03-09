from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypeVoucherType7(Enum):
    FULL_CREDIT = "FullCredit"
    GROUP_OR_DAY = "GroupOrDay"
    SPECIFIC_VALUE = "SpecificValue"
    REGULAR_VOUCHER = "RegularVoucher"
