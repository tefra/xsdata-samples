from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .duty_part import DutyPart
from .duty_part_ref import DutyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dutyParts_RelStructure"

    duty_part_ref: List[DutyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_part: List[DutyPart] = field(
        default_factory=list,
        metadata={
            "name": "DutyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
