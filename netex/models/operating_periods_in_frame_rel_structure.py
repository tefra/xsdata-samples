from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .operating_period_1 import OperatingPeriod1
from .uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingPeriodsInFrame_RelStructure"

    operating_period_or_uic_operating_period: List[
        Union[OperatingPeriod1, UicOperatingPeriod]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
