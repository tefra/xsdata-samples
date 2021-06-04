from dataclasses import dataclass
from netex.models.version_version_structure import VersionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Version(VersionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
