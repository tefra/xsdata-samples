from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.humidity import Humidity
from datexii.models.eu.datexii.v2.weather_data import WeatherData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class HumidityInformation(WeatherData):
    """
    Measurements of atmospheric humidity.
    """

    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
