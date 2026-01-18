from dataclasses import dataclass, field
from typing import Optional, Union

from .direction_ref import DirectionRef
from .external_object_ref_structure import ExternalObjectRefStructure
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineInDirectionRefStructure:
    class Meta:
        name = "LineInDirectionRef_Structure"

    line_ref: FlexibleLineRef | LineRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_ref: DirectionRef | None = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_line_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_direction_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
