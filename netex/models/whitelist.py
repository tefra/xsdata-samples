from dataclasses import dataclass

from .whitelist_version_structure import WhitelistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Whitelist(WhitelistVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
