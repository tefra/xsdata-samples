from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.geographical_interval import GeographicalInterval
from netex.models.geographical_interval_ref import GeographicalIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "geographicalIntervals_RelStructure"

    geographical_interval_ref: List[GeographicalIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval: List[GeographicalInterval] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
