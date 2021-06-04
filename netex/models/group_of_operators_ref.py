from dataclasses import dataclass
from netex.models.group_of_operators_ref_structure import GroupOfOperatorsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfOperatorsRef(GroupOfOperatorsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
