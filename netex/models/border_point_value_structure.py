from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_operators import GroupOfOperators
from .group_of_operators_ref import GroupOfOperatorsRef
from .multilingual_string import MultilingualString
from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointValueStructure(TimingPointVersionStructure):
    class Meta:
        name = "BorderPoint_ValueStructure"

    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_operators_ref_or_group_of_operators: (
        None | GroupOfOperatorsRef | GroupOfOperators
    ) = field(
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
        },
    )
