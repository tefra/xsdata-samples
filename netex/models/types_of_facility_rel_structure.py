from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_facility import TypeOfFacility
from .type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfFacilityRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfFacility_RelStructure"

    type_of_facility_ref_or_type_of_facility: Iterable[
        TypeOfFacilityRef | TypeOfFacility
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFacilityRef",
                    "type": TypeOfFacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
