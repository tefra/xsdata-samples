from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PartialRefundBasisEnumeration(StrEnum):
    UNUSED_DAYS = "unusedDays"
    UNUSED_WEEKS = "unusedWeeks"
    UNUSED_MONTHS = "unusedMonths"
    UNUSED_SEMESTERS = "unusedSemesters"
    OTHER = "other"
