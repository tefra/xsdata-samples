from dataclasses import dataclass, field
from typing import List
from .authority_ref import AuthorityRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operator_ref import OperatorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transportOrganisationRefs_RelStructure"

    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
