from dataclasses import dataclass, field
from typing import List
from .authority_ref import AuthorityRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operator_ref import OperatorRef
from .transport_organisation_ref import TransportOrganisationRef

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
            "min_occurs": 1,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
