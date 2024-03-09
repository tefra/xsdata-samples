from dataclasses import dataclass

from .all_authorities_ref_structure import AllAuthoritiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllAuthoritiesRef(AllAuthoritiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
