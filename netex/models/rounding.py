from dataclasses import dataclass

from .rounding_versioned_structure import RoundingVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Rounding(RoundingVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
