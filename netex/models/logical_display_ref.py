from dataclasses import dataclass
from netex.models.logical_display_ref_structure import LogicalDisplayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogicalDisplayRef(LogicalDisplayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
