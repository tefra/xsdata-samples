from dataclasses import dataclass, field
from typing import Optional
from .accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityTool:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[AccessibilityToolEnumeration] = field(
        default=None
    )
