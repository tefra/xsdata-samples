from dataclasses import dataclass, field
from typing import Optional
from .dated_special_service_ref import DatedSpecialServiceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "specialServiceRefs_RelStructure"

    dated_special_service_ref: Optional[DatedSpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    special_service_ref: Optional[SpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
