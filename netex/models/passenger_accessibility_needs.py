from dataclasses import dataclass

from .passenger_accessibility_needs_structure import (
    PassengerAccessibilityNeedsStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerAccessibilityNeeds(PassengerAccessibilityNeedsStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
