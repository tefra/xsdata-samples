from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.distance_along_linear_element import (
    DistanceAlongLinearElement,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.height_grade_enum import HeightGradeEnum
from datexii.models.eu.datexii.v2.linear_element import LinearElement
from datexii.models.eu.datexii.v2.linear_referencing_direction_enum import (
    LinearReferencingDirectionEnum,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointAlongLinearElement:
    """
    A point on a linear element where the linear element is either a part
    of or the whole of a linear object (i.e. a road), consistent with ISO
    19148 definitions.

    :ivar administrative_area_of_point: Identification of the road
        administration area which contains the specified point.
    :ivar direction_bound_at_point: The direction of traffic flow at the
        specified point in terms of general destination direction.
    :ivar direction_relative_at_point: The direction of traffic flow at
        the specified point relative to the direction in which the
        linear element is defined.
    :ivar height_grade_of_point: Identification of whether the point on
        the linear element is at, above or below the normal elevation of
        a linear element of that type (e.g. road or road section) at
        that location, typically used to indicate "grade" separation.
    :ivar linear_element:
    :ivar distance_along_linear_element:
    :ivar point_along_linear_element_extension:
    """

    administrative_area_of_point: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    direction_bound_at_point: DirectionEnum | None = field(
        default=None,
        metadata={
            "name": "directionBoundAtPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    direction_relative_at_point: LinearReferencingDirectionEnum | None = (
        field(
            default=None,
            metadata={
                "name": "directionRelativeAtPoint",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    height_grade_of_point: HeightGradeEnum | None = field(
        default=None,
        metadata={
            "name": "heightGradeOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    linear_element: LinearElement | None = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    distance_along_linear_element: DistanceAlongLinearElement | None = (
        field(
            default=None,
            metadata={
                "name": "distanceAlongLinearElement",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    point_along_linear_element_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "pointAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
