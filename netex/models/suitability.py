from dataclasses import dataclass
from .suitability_versioned_child_structure import (
    SuitabilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Suitability(SuitabilityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
