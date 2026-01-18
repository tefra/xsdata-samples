from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_functional_road_class_enum import (
    OpenlrFunctionalRoadClassEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPathAttributes:
    """
    The field path attributes is part of a location reference point (except
    for the last location reference point) and consists of lowest
    functional road class (LFRCNP) and distance to next point (DNP) data.

    :ivar openlr_lowest_frcto_next_lrpoint: The lowest FRC to the next
        point indicates the lowest functional road class used in the
        location reference path to the next LR-point.
    :ivar openlr_distance_to_next_lrpoint: The DNP attribute measures
        the distance in meters between two consecutive LR-points along
        the location reference path as described in the logical format.
    :ivar openlr_path_attributes_extension:
    """

    openlr_lowest_frcto_next_lrpoint: None | OpenlrFunctionalRoadClassEnum = (
        field(
            default=None,
            metadata={
                "name": "openlrLowestFRCToNextLRPoint",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    openlr_distance_to_next_lrpoint: None | int = field(
        default=None,
        metadata={
            "name": "openlrDistanceToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_path_attributes_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "openlrPathAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
