from dataclasses import dataclass
from .version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionRef(VersionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
