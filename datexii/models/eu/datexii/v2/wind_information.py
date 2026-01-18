from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.weather_data import WeatherData
from datexii.models.eu.datexii.v2.wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class WindInformation(WeatherData):
    """
    Measurements of wind conditions.
    """

    wind: Wind = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    wind_information_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
