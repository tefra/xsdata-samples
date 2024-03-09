from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .operating_period_1 import OperatingPeriod1
from .operating_period_ref import OperatingPeriodRef
from .uic_operating_period import UicOperatingPeriod
from .uic_operating_period_ref import UicOperatingPeriodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingPeriods_RelStructure"

    choice: List[
        Union[
            UicOperatingPeriodRef,
            OperatingPeriodRef,
            OperatingPeriod1,
            UicOperatingPeriod,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
