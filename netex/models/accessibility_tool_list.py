from dataclasses import dataclass, field
from typing import List
from .accessibility_tool_enumeration import AccessibilityToolEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityToolList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
