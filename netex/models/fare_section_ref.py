from dataclasses import dataclass

from .fare_section_ref_structure import FareSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareSectionRef(FareSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
