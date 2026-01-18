from __future__ import annotations

from dataclasses import dataclass, field

from .accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityTool:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityToolEnumeration = field(
        metadata={
            "required": True,
        }
    )
