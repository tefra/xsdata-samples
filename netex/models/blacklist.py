from dataclasses import dataclass

from .blacklist_version_structure import BlacklistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Blacklist(BlacklistVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
