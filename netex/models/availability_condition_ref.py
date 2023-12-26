from dataclasses import dataclass
from .availability_condition_ref_structure import (
    AvailabilityConditionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AvailabilityConditionRef(AvailabilityConditionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
