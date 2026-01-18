from __future__ import annotations

from dataclasses import dataclass, field

from .accessibility_limitation import AccessibilityLimitation
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityLimitationsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "accessibilityLimitations_RelStructure"

    accessibility_limitation: AccessibilityLimitation = field(
        metadata={
            "name": "AccessibilityLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
