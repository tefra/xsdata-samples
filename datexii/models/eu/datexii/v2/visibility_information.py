from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.visibility import Visibility
from datexii.models.eu.datexii.v2.weather_data import WeatherData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VisibilityInformation(WeatherData):
    """
    Measurements of atmospheric visibility.
    """

    visibility: Visibility = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    visibility_information_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
