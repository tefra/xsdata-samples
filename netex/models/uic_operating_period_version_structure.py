from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .day_of_week_enumeration import DayOfWeekEnumeration
from .operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UicOperatingPeriodVersionStructure(OperatingPeriodVersionStructure):
    class Meta:
        name = "UicOperatingPeriod_VersionStructure"

    valid_day_bits: str = field(
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    days_of_week: Iterable[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
