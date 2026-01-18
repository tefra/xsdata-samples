from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.floating_point_metre_distance_value import (
    FloatingPointMetreDistanceValue,
)
from datexii.models.eu.datexii.v2.precipitation_intensity_value import (
    PrecipitationIntensityValue,
)
from datexii.models.eu.datexii.v2.precipitation_type_enum import (
    PrecipitationTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PrecipitationDetail:
    """
    Details of precipitation (rain, snow etc.).

    :ivar precipitation_type: The type of precipitation which is
        affecting the driving conditions.
    :ivar precipitation_intensity: The height of the precipitation
        received per unit time.
    :ivar deposition_depth: The equivalent depth of the water layer
        resulting from precipitation or deposition on a non-porous
        horizontal surface. Non liquid precipitation is considered as
        melted in water form.
    :ivar precipitation_detail_extension:
    """

    precipitation_type: None | PrecipitationTypeEnum = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    precipitation_intensity: None | PrecipitationIntensityValue = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    deposition_depth: None | FloatingPointMetreDistanceValue = field(
        default=None,
        metadata={
            "name": "depositionDepth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    precipitation_detail_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "precipitationDetailExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
