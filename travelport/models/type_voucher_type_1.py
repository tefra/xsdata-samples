from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeVoucherType1(StrEnum):
    FULL_CREDIT = "FullCredit"
    GROUP_OR_DAY = "GroupOrDay"
    SPECIFIC_VALUE = "SpecificValue"
    REGULAR_VOUCHER = "RegularVoucher"
