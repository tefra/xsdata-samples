from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.openlr_line_location_reference import (
    OpenlrLineLocationReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class OpenlrExtendedLinear:
    """
    Extension class for OpenLR Line location reference.

    :ivar first_direction: First OpenLR reference in first/main
        direction.
    :ivar opposite_direction: If both direction, this is tha reference
        in the opposite direction against firstDirection.
    """

    first_direction: OpenlrLineLocationReference = field(
        metadata={
            "name": "firstDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    opposite_direction: None | OpenlrLineLocationReference = field(
        default=None,
        metadata={
            "name": "oppositeDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
