from dataclasses import dataclass
from netex.models.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineRef(LineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
