from dataclasses import dataclass, field
from typing import List
from netex.models.access_zone import AccessZone
from netex.models.access_zone_ref import AccessZoneRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessZonesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessZones_RelStructure"

    access_zone_ref: List[AccessZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_zone: List[AccessZone] = field(
        default_factory=list,
        metadata={
            "name": "AccessZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
