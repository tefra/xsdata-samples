from __future__ import annotations

from dataclasses import dataclass

from .operating_period_ref_structure import OperatingPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UicOperatingPeriodRefStructure(OperatingPeriodRefStructure):
    pass
