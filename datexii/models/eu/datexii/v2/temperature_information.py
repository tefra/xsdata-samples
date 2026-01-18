from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.temperature import Temperature
from datexii.models.eu.datexii.v2.weather_data import WeatherData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TemperatureInformation(WeatherData):
    """
    Measurements of atmospheric temperature.
    """

    temperature: Temperature | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    temperature_information_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
