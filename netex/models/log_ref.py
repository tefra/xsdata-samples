from dataclasses import dataclass
from netex.models.log_ref_structure import LogRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogRef(LogRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
