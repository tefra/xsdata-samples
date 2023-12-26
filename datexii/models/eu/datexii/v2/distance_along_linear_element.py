from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DistanceAlongLinearElement:
    """
    Distance of a point along a linear element either measured from the start node
    or a defined referent on that linear element, where the start node is relative
    to the element definition rather than the direction of traffic flow.
    """

    distance_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "distanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
