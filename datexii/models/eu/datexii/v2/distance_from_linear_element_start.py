from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.distance_along_linear_element import (
    DistanceAlongLinearElement,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DistanceFromLinearElementStart(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node of the
    linear element, where start node is relative to the element definition rather
    than the direction of traffic flow.

    :ivar distance_along: A measure of distance along a linear element.
    :ivar distance_from_linear_element_start_extension:
    """

    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    distance_from_linear_element_start_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "distanceFromLinearElementStartExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
