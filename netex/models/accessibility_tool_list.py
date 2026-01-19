from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityToolList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
