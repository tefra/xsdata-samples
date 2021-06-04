from dataclasses import dataclass
from netex.models.default_connection_version_structure import DefaultConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultConnection(DefaultConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
