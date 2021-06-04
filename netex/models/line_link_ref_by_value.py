from dataclasses import dataclass
from netex.models.line_link_ref_by_value_structure import LineLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineLinkRefByValue(LineLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
