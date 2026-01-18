from __future__ import annotations

from dataclasses import dataclass

from .usage_validity_period_ref_structure import (
    UsageValidityPeriodRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageValidityPeriodRef(UsageValidityPeriodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
