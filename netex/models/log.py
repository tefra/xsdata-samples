from dataclasses import dataclass
from netex.models.log_version_structure import LogVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Log(LogVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
