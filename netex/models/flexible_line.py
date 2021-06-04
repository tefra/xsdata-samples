from dataclasses import dataclass
from netex.models.flexible_line_version_structure import FlexibleLineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLine(FlexibleLineVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
