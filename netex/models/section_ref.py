from dataclasses import dataclass
from netex.models.section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SectionRef(SectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
