from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.road_conditions import RoadConditions
from datexii.models.eu.datexii.v2.road_surface_condition_measurements import (
    RoadSurfaceConditionMeasurements,
)
from datexii.models.eu.datexii.v2.weather_related_road_condition_type_enum import (
    WeatherRelatedRoadConditionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class WeatherRelatedRoadConditions(RoadConditions):
    """
    Road surface conditions that are related to the weather which may
    affect the driving conditions, such as ice, snow or water.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar weather_related_road_conditions_extension:
    """

    weather_related_road_condition_type: list[
        WeatherRelatedRoadConditionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    road_surface_condition_measurements: RoadSurfaceConditionMeasurements | None = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    weather_related_road_conditions_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
