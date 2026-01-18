from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.application_rate_value import (
    ApplicationRateValue,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.floating_point_metre_distance_value import (
    FloatingPointMetreDistanceValue,
)
from datexii.models.eu.datexii.v2.kilograms_concentration_value import (
    KilogramsConcentrationValue,
)
from datexii.models.eu.datexii.v2.temperature_value import TemperatureValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadSurfaceConditionMeasurements:
    """
    Measurements of the road surface condition which relate specifically to
    the weather.

    :ivar road_surface_temperature: The temperature measured on the road
        surface.
    :ivar protection_temperature: The road surface temperature down to
        which the surface is protected from freezing.
    :ivar de_icing_application_rate: Indicates the rate at which de-
        icing agents have been applied to the specified road.
    :ivar de_icing_concentration: Indicates the concentration of de-
        icing agent present in surface water on the specified road.
    :ivar depth_of_snow: The depth of snow recorded on the road surface.
    :ivar water_film_thickness: The depth of standing water to be found
        on the road surface.
    :ivar road_surface_condition_measurements_extension:
    """

    road_surface_temperature: TemperatureValue | None = field(
        default=None,
        metadata={
            "name": "roadSurfaceTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    protection_temperature: TemperatureValue | None = field(
        default=None,
        metadata={
            "name": "protectionTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    de_icing_application_rate: ApplicationRateValue | None = field(
        default=None,
        metadata={
            "name": "deIcingApplicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    de_icing_concentration: KilogramsConcentrationValue | None = field(
        default=None,
        metadata={
            "name": "deIcingConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    depth_of_snow: FloatingPointMetreDistanceValue | None = field(
        default=None,
        metadata={
            "name": "depthOfSnow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    water_film_thickness: FloatingPointMetreDistanceValue | None = field(
        default=None,
        metadata={
            "name": "waterFilmThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    road_surface_condition_measurements_extension: ExtensionType | None = (
        field(
            default=None,
            metadata={
                "name": "roadSurfaceConditionMeasurementsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
