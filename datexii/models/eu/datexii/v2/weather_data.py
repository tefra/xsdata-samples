from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class WeatherData(BasicData):
    """
    Measured or derived values relating to the weather at a specific
    location or locations.
    """

    weather_data_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "weatherDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
