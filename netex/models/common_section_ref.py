from dataclasses import dataclass
from .common_section_ref_structure import CommonSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonSectionRef(CommonSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
