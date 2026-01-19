from __future__ import annotations

from dataclasses import dataclass, field

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
