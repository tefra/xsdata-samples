from dataclasses import dataclass
from .alternative_quay_descriptor_versioned_child_structure import AlternativeQuayDescriptorVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeQuayDescriptor(AlternativeQuayDescriptorVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
