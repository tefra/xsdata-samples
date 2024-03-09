from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.distance_along_linear_element import (
    DistanceAlongLinearElement,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PercentageDistanceAlongLinearElement(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node
    expressed as a percentage of the whole length of the linear element, where
    start node is relative to the element definition rather than the direction of
    traffic flow.

    :ivar percentage_distance_along: A measure of distance along a
        linear element from the start of the element expressed as a
        percentage of the total length of the linear object.
    :ivar percentage_distance_along_linear_element_extension:
    """

    percentage_distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentageDistanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    percentage_distance_along_linear_element_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "percentageDistanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
