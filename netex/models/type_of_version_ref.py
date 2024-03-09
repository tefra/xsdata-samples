from dataclasses import dataclass

from .type_of_version_ref_structure import TypeOfVersionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfVersionRef(TypeOfVersionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
