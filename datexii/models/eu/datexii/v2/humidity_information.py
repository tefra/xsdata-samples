from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.humidity import Humidity
from datexii.models.eu.datexii.v2.weather_data import WeatherData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class HumidityInformation(WeatherData):
    """
    Measurements of atmospheric humidity.
    """

    humidity: Humidity = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    humidity_information_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
