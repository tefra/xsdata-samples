from dataclasses import dataclass
from netex.models.line_section_ref_structure import LineSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineSectionRef(LineSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
