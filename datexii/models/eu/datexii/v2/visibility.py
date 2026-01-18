from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.integer_metre_distance_value import (
    IntegerMetreDistanceValue,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class Visibility:
    """
    Details of atmospheric visibility.

    :ivar minimum_visibility_distance: The minimum distance, measured or
        estimated, beyond which drivers may be unable to clearly see a
        vehicle or an obstacle.
    :ivar visibility_extension:
    """

    minimum_visibility_distance: IntegerMetreDistanceValue = field(
        metadata={
            "name": "minimumVisibilityDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    visibility_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "visibilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
