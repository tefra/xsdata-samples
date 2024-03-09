from dataclasses import dataclass

from .security_list_version_structure import SecurityListVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityList(SecurityListVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
