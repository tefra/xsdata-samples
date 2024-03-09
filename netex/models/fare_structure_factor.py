from dataclasses import dataclass
from .priceable_object_version_structure import (
    FareStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureFactor(FareStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
