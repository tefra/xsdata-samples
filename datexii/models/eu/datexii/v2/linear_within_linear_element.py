from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.distance_along_linear_element import DistanceAlongLinearElement
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.height_grade_enum import HeightGradeEnum
from datexii.models.eu.datexii.v2.linear_element import LinearElement
from datexii.models.eu.datexii.v2.linear_referencing_direction_enum import LinearReferencingDirectionEnum
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearWithinLinearElement:
    """
    A linear section along a linear element where the linear element is either a
    part of or the whole of a linear object (i.e. a road), consistent with ISO
    19148 definitions.

    :ivar administrative_area_of_linear_section: Identification of the
        road administration area which contains the specified linear
        section.
    :ivar direction_bound_on_linear_section: The direction of traffic
        flow on the linear section in terms of general destination
        direction.
    :ivar direction_relative_on_linear_section: The direction of traffic
        flow on the linear section relative to the direction in which
        the linear element is defined.
    :ivar height_grade_of_linear_section: Identification of whether the
        linear section that is part of the linear element is at, above
        or below the normal elevation of a linear element of that type
        (e.g. road or road section) at that location, typically used to
        indicate "grade" separation.
    :ivar linear_element:
    :ivar from_point: A point on the linear element that defines the
        start node of the linear section.
    :ivar to_point: A point on the linear element that defines the end
        node of the linear section.
    :ivar linear_within_linear_element_extension:
    """
    administrative_area_of_linear_section: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_bound_on_linear_section: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBoundOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    direction_relative_on_linear_section: Optional[LinearReferencingDirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionRelativeOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    height_grade_of_linear_section: Optional[HeightGradeEnum] = field(
        default=None,
        metadata={
            "name": "heightGradeOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    linear_element: Optional[LinearElement] = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "fromPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    to_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "toPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    linear_within_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearWithinLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
