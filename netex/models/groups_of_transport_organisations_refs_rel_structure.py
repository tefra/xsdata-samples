from dataclasses import dataclass, field
from typing import List
from netex.models.group_of_operators_ref import GroupOfOperatorsRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfTransportOrganisationsRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupsOfTransportOrganisationsRefs_RelStructure"

    group_of_operators_ref: List[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
