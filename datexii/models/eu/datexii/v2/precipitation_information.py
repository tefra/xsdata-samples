from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.precipitation_detail import (
    PrecipitationDetail,
)
from datexii.models.eu.datexii.v2.weather_data import WeatherData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PrecipitationInformation(WeatherData):
    """
    Measurements of precipitation.

    :ivar no_precipitation: Indication of whether precipitation is
        present or not. True indicates there is no precipitation.
    :ivar precipitation_detail:
    :ivar precipitation_information_extension:
    """

    no_precipitation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPrecipitation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    precipitation_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
