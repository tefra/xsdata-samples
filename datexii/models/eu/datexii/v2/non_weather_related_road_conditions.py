from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.non_weather_related_road_condition_type_enum import (
    NonWeatherRelatedRoadConditionTypeEnum,
)
from datexii.models.eu.datexii.v2.road_conditions import RoadConditions

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonWeatherRelatedRoadConditions(RoadConditions):
    """
    Road surface conditions that are not related to the weather but which may
    affect driving conditions.

    :ivar non_weather_related_road_condition_type: The type of road
        conditions which are not related to the weather.
    :ivar non_weather_related_road_conditions_extension:
    """

    non_weather_related_road_condition_type: list[
        NonWeatherRelatedRoadConditionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "nonWeatherRelatedRoadConditionsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
