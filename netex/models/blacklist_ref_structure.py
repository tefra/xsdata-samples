from dataclasses import dataclass

from .security_list_ref_structure import SecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistRefStructure(SecurityListRefStructure):
    pass
