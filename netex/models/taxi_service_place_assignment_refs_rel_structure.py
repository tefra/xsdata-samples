from dataclasses import dataclass, field
from typing import Optional

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .taxi_service_place_assignment_ref import TaxiServicePlaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServicePlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "TaxiServicePlaceAssignmentRefs_RelStructure"

    taxi_service_place_assignment_ref: Optional[
        TaxiServicePlaceAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "TaxiServicePlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
