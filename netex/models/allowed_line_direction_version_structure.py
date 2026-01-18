from dataclasses import dataclass, field
from typing import Optional, Union

from .direction_ref import DirectionRef
from .entity_in_version_structure import DataManagedObjectStructure
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .presentation_structure import PresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AllowedLineDirection_VersionStructure"

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
            "required": True,
        },
    )
    presentation: PresentationStructure | None = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
