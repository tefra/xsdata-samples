from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfServiceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfServiceRefs_RelStructure"

    type_of_service_ref: Iterable[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
