from dataclasses import dataclass
from .sections_in_sequence_rel_structure import SectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Section1(SectionVersionStructure):
    class Meta:
        name = "Section"
        namespace = "http://www.netex.org.uk/netex"
