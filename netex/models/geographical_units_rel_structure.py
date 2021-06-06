from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .geographical_unit import GeographicalUnit
from .geographical_unit_ref import GeographicalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "geographicalUnits_RelStructure"

    geographical_unit_ref: List[GeographicalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit: List[GeographicalUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
