from dataclasses import dataclass
from .accessibility_limitation_versioned_child_structure import AccessibilityLimitationVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityLimitation(AccessibilityLimitationVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
