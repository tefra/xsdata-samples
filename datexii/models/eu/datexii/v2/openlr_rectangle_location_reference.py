from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_rectangle import OpenlrRectangle

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrRectangleLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing a rectangular shape
    defined by two geo-coordinate pairs.
    """

    openlr_rectangle: None | OpenlrRectangle = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_rectangle_location_reference_extension: None | ExtensionType = (
        field(
            default=None,
            metadata={
                "name": "openlrRectangleLocationReferenceExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
