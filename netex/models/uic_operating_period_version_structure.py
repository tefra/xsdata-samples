from dataclasses import dataclass, field
from typing import List, Optional
from .day_of_week_enumeration import DayOfWeekEnumeration
from .operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicOperatingPeriodVersionStructure(OperatingPeriodVersionStructure):
    class Meta:
        name = "UicOperatingPeriod_VersionStructure"

    valid_day_bits: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
