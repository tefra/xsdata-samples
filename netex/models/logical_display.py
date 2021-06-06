from dataclasses import dataclass
from .logical_display_version_structure import LogicalDisplayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogicalDisplay(LogicalDisplayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
