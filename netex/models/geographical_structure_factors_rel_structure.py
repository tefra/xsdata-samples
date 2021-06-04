from dataclasses import dataclass, field
from typing import List
from netex.models.geographical_structure_factor import GeographicalStructureFactor
from netex.models.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "geographicalStructureFactors_RelStructure"

    geographical_structure_factor_ref: List[GeographicalStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factor: List[GeographicalStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
