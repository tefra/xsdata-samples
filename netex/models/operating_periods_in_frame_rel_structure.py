from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.operating_period import OperatingPeriod
from netex.models.uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingPeriodsInFrame_RelStructure"

    operating_period: List[OperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "OperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    uic_operating_period: List[UicOperatingPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UicOperatingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
