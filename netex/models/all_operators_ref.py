from dataclasses import dataclass
from .all_operators_ref_structure import AllOperatorsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllOperatorsRef(AllOperatorsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
