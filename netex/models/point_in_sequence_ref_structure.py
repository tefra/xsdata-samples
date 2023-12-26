from dataclasses import dataclass
from .ordered_version_of_object_ref_structure import (
    OrderedVersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointInSequenceRefStructure(OrderedVersionOfObjectRefStructure):
    pass
