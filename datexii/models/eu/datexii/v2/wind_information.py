from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.weather_data import WeatherData
from datexii.models.eu.datexii.v2.wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class WindInformation(WeatherData):
    """
    Measurements of wind conditions.
    """

    wind: Wind | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    wind_information_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
