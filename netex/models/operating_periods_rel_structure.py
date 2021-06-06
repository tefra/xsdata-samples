from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .operating_period import OperatingPeriod
from .operating_period_ref import OperatingPeriodRef
from .uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingPeriods_RelStructure"

    operating_period_ref: List[OperatingPeriodRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
