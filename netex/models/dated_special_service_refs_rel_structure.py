from dataclasses import dataclass, field

from .dated_special_service_ref import DatedSpecialServiceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedSpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "DatedSpecialServiceRefs_RelStructure"

    dated_special_service_ref: DatedSpecialServiceRef | None = field(
        default=None,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
