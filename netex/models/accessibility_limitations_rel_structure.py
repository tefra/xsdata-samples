from dataclasses import dataclass, field
from typing import Optional

from .accessibility_limitation import AccessibilityLimitation
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityLimitationsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "accessibilityLimitations_RelStructure"

    accessibility_limitation: AccessibilityLimitation | None = field(
        default=None,
        metadata={
            "name": "AccessibilityLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
