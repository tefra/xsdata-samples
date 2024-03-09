from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .duty_part import DutyPart
from .duty_part_ref import DutyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dutyParts_RelStructure"

    duty_part_ref_or_duty_part: List[Union[DutyPartRef, DutyPart]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DutyPartRef",
                    "type": DutyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPart",
                    "type": DutyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
