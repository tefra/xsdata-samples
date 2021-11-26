from dataclasses import dataclass
from .link_sequence_version_structure import SectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Section1(SectionVersionStructure):
    class Meta:
        name = "Section"
        namespace = "http://www.netex.org.uk/netex"
