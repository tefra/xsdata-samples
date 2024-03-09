from dataclasses import dataclass, field
from typing import List, Union

from .geographical_structure_factor import GeographicalStructureFactor
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalStructureFactorsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "geographicalStructureFactors_RelStructure"

    geographical_structure_factor_ref_or_geographical_structure_factor: List[
        Union[GeographicalStructureFactorRef, GeographicalStructureFactor]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
