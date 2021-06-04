from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.journey_accounting import JourneyAccounting
from netex.models.journey_accounting_ref import JourneyAccountingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccountingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyAccountings_RelStructure"

    journey_accounting_ref: List[JourneyAccountingRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccountingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accounting: List[JourneyAccounting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccounting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
