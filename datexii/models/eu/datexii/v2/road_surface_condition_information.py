from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.road_surface_condition_measurements import RoadSurfaceConditionMeasurements
from datexii.models.eu.datexii.v2.weather_data import WeatherData
from datexii.models.eu.datexii.v2.weather_related_road_condition_type_enum import WeatherRelatedRoadConditionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadSurfaceConditionInformation(WeatherData):
    """
    Measurements of road surface conditions which are related to the weather.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar road_surface_condition_information_extension:
    """
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    road_surface_condition_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
