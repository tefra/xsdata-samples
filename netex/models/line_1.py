from dataclasses import dataclass
from netex.models.line_version_structure import LineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Line1(LineVersionStructure):
    class Meta:
        name = "Line"
        namespace = "http://www.netex.org.uk/netex"
