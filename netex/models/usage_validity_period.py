from __future__ import annotations

from dataclasses import dataclass

from .usage_validity_period_version_structure import (
    UsageValidityPeriodVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageValidityPeriod(UsageValidityPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
