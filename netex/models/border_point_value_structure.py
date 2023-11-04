from dataclasses import dataclass, field
from typing import Optional, Union
from .group_of_operators import GroupOfOperators
from .group_of_operators_ref import GroupOfOperatorsRef
from .multilingual_string import MultilingualString
from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BorderPointValueStructure(TimingPointVersionStructure):
    class Meta:
        name = "BorderPoint_ValueStructure"

    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_operators_ref_or_group_of_operators: Optional[Union[GroupOfOperators, GroupOfOperatorsRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperators",
                    "type": GroupOfOperators,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
