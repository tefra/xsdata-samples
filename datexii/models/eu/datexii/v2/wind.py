from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.direction_bearing_value import (
    DirectionBearingValue,
)
from datexii.models.eu.datexii.v2.direction_compass_value import (
    DirectionCompassValue,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.speed_value import SpeedValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Wind:
    """
    Wind conditions on the road.

    :ivar wind_measurement_height: The height in metres above the road
        surface at which the wind is measured.
    :ivar wind_speed: The wind speed averaged over at least 10 minutes,
        measured at a default height of10 metres (meteorological
        standard) above the road surface, unless measurement height is
        specified.
    :ivar maximum_wind_speed: The maximum wind speed in a measurement
        period of 10 minutes.
    :ivar wind_direction_bearing: The average direction from which the
        wind blows, in terms of a bearing measured in degrees (0 - 359).
    :ivar wind_direction_compass: The average direction from which the
        wind blows, in terms of points of the compass.
    :ivar wind_extension:
    """

    wind_measurement_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "windMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    wind_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_wind_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "maximumWindSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    wind_direction_bearing: Optional[DirectionBearingValue] = field(
        default=None,
        metadata={
            "name": "windDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    wind_direction_compass: Optional[DirectionCompassValue] = field(
        default=None,
        metadata={
            "name": "windDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    wind_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
