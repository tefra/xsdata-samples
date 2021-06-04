from dataclasses import dataclass
from netex.models.group_of_operators_structure import GroupOfOperatorsStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfOperators(GroupOfOperatorsStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
