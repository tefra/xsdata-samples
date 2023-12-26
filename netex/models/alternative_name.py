from dataclasses import dataclass
from .alternative_name_versioned_child_structure import (
    AlternativeNameVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeName(AlternativeNameVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
