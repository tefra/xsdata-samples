from dataclasses import dataclass

from .connection_version_structure import ConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Connection(ConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
