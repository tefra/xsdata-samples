from dataclasses import dataclass
from netex.models.class_ref_structure import ClassRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassRef(ClassRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
