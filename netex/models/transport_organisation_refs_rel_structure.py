from dataclasses import dataclass, field
from typing import List, Union

from .authority_ref import AuthorityRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operator_ref import OperatorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transportOrganisationRefs_RelStructure"

    transport_organisation_ref: List[Union[AuthorityRef, OperatorRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
